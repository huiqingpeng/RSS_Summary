---
title: "How to Build Deep Agents for Enterprise Search with NVIDIA AI-Q and LangChain"
source: "NVIDIA Developer Blog"
url: "https://developer.nvidia.com/blog/how-to-build-deep-agents-for-enterprise-search-with-nvidia-ai-q-and-langchain/"
published: "2026-03-18"
fetched: "2026-03-19T00:03:03.136127"
---

While consumer AI offers powerful capabilities, workplace tools often suffer from disjointed data and limited context. Built with LangChain, the NVIDIA AI-Q blueprint is an open source template that bridges this gap. LangChain recently introduced an enterprise agent platform built with NVIDIA AI to support scalable, production-ready agent development.
This tutorial, available as an NVIDIA launchable, shows developers how to use the AI-Q blueprint to create a deep research agent that tops leaderboards and can be connected to enterprise systems. The blueprint uses the best of open and frontier LLMs, is optimized using the NVIDIA NeMo Agent Toolkit, and monitored with LangSmith. The result: faster time-to-production for agentic search apps that keep business data exactly where it belongs—private and in a secure environment.
The NVIDIA AI-Q blueprint and NeMo Agent Toolkit are both part of the broader NVIDIA Agent Toolkit, a collection of tools, models and runtimes for building, evaluating and optimizing safe, long-running autonomous agents.
What you’ll build: A deep agent
You will learn:
- How to deploy the NVIDIA AI‑Q blueprint with LangChain for enterprise search use cases
- How to configure shallow and deep research agents using Nemotron and frontier LLMs
- How to monitor agent traces and performance with LangSmith and NVIDIA tools
- How to connect internal enterprise data sources through NeMo Agent Toolkit tools
Set up
- NVIDIA API Key for access to open models such as Nemotron 3
- OpenAI API Key for access to a frontier model such as GPT-5.2
- Tavily API Key for web search
- Python
- Docker Compose
- Optional: LangSmith for monitoring and experiment tracking
How to build long-running data agents with NVIDIA and LangChain
Install and run the blueprint
Clone the repository and configure your API keys. Copy the environment template first.
cp deploy/.env.example deploy/.env
Open deploy/.env
and fill in the required values.
# Required
NVIDIA_API_KEY=nvapi-...
TAVILY_API_KEY=tvly-...
# Optional: enables trace monitoring (covered later in this post)
LANGSMITH_API_KEY=lsv2-...
The NVIDIA_API_KEY
grants access to NVIDIA-hosted models like Nemotron 3 Nano. The TAVILY_API_KEY
enables web search.
Next, build and start the full stack. Starting multiple containers at once means the first build can take a few minutes, based on your internet connection and hardware specs.
docker compose -f deploy/compose/docker-compose.yaml up --build
This launches three services:
- aiq-research-assistant: The FastAPI backend on port 8000
- postgres: PostgreSQL 16 for async job state and conversation checkpoints
- frontend: The Next.js web UI on port 3000
Once all services report healthy, open http://localhost:3000. Figure 1, below, shows the AI-Q Research Assistant chat interface, where you type a research query and watch the agent work in real time.
Customize AI-Q: Workflow, tracing and model configuration
Open configs/config_web_docker.yml
. This single file controls the LLMs, tools, agents, and workflow configuration.
The llms
section declares named models. Notice the enable_thinking
flag—it toggles chain-of-thought reasoning on or off for Nemotron. The following example declares three LLMs with different roles:
llms:
nemotron_llm_non_thinking:
_type: nim
model_name: nvidia/nemotron-3-super-120b-a12b
temperature: 0.7
max_tokens: 8192
chat_template_kwargs:
enable_thinking: false
nemotron_llm:
_type: nim
model_name: nvidia/nemotron-3-super-120b-a12b
temperature: 1.0
max_tokens: 100000
chat_template_kwargs:
enable_thinking: true
gpt-5-2:
_type: openai
model_name: 'gpt-5.2'
nemotron_llm_non_thinking
handles fast responses where chain-of-thought adds latency without benefit. nemotron_llm
enables thinking mode with a 100K context window for the agents that need multi-step reasoning. gpt-5.2
adds a frontier model for orchestration.
The blueprint consists of both a shallow and deep research agent. The following configuration shows both:
functions:
shallow_research_agent:
_type: shallow_research_agent
llm: nemotron_llm
tools:
- web_search_tool
max_llm_turns: 10
max_tool_calls: 5
deep_research_agent:
_type: deep_research_agent
orchestrator_llm: gpt-5
planner_llm: nemotron_llm
researcher_llm: nemotron_llm
max_loops: 2
tools:
- advanced_web_search_tool
The shallow research agent runs a bounded tool-calling loop—up to 10 LLM turns and 5 tool calls—then returns a concise answer with citations. Simple questions like “What is CUDA?” resolve in seconds. The deep research agent uses a LangChain deep agent with a ToDo list, file system, and sub-agents to produce long-form, citation-backed reports.
To keep all inference on-premise, change the orchestrator_llm to point at a self-hosted model.
Monitor the traces
To monitor AI‑Q agents, enable LangSmith tracing so each query generates a full execution trace, including LangChain tool calls and model usage. Add your LANGSMITH_API_KEY
to your deploy/.env
and add the telemetry section to the config file:
general:
telemetry:
tracing:
langsmith:
_type: langsmith
project: aiq-gtc-demo
api_key: ${LANGSMITH_API_KEY}
Each query generates a trace that captures the full execution path.
Shallow research sample query:
What is the deepest place on earth?
Deep research sample query:
Analyze the current 2026 scientific consensus on the deepest points on Earth, comparing the Challenger Deep in the Mariana Trench to terrestrial extremes such as the Veryovkina Cave and the Kola Superdeep Borehole. Include the latest bathymetric and geodetic measurements, an assessment of measurement uncertainties (including gravity and pressure sensor corrections), and a summary of recent deep-sea expeditions from 2020–2026 that have updated our understanding of the Hadal zone's topography and biological life.
Expand the trace to inspect each node. The tool calls to web search are especially useful for debugging—you can see exactly what query the agent sent and what results came back. Beyond individual traces, use LangSmith to track latency, token usage, and error rates over time, and set alerts for regressions.
Optimize a deep agent
To tune the deep research agent for your domain, start by examining how it assembles its sub-agents. The deep research agent uses the create_deep_agent
factory from LangChain’s deepagents
library.
from deepagents import create_deep_agent
return create_deep_agent(
model=self.llm_provider.get(LLMRole.ORCHESTRATOR),
system_prompt=orchestrator_prompt,
tools=self.tools,
subagents=self.subagents,
middleware=custom_middleware,
skills=self.skills,
).with_config({"recursion_limit": 1000})
The factory wires together the orchestrator LLM, the tools, and two sub-agents.
self.subagents = [
{
"name": "planner-agent",
"system_prompt": render_prompt_template(
self._prompts["planner"], tools=self.tools_info,
),
"tools": self.tools,
"model": self.llm_provider.get(LLMRole.PLANNER),
},
{
"name": "researcher-agent",
"system_prompt": render_prompt_template(
self._prompts["researcher"], tools=self.tools_info,
),
"tools": self.tools,
"model": self.llm_provider.get(LLMRole.RESEARCHER),
},
]
Context management is central to how deep agents work. The planner agent produces a JSON research plan. The researcher agent receives only this plan — not the orchestrator’s thinking tokens or the planner’s internal reasoning. By passing only a structured payload, we reduce the token bloat and prevent the “lost in the middle” phenomenon, where LLMs forget critical instructions buried deep in massive context windows. This isolation keeps each sub-agent focused. The following example shows a planner output for a query about retrieval-augmented generation (RAG) versus long-context approaches:
{
"report_title": "RAG vs Long-Context Models for Enterprise Search",
"report_toc": [
{
"id": "1",
"title": "Architectural Foundations",
"subsections": [
{"id": "1.1", "title": "Retrieval-Augmented Generation Pipeline"},
{"id": "1.2", "title": "Long-Context Transformer Architectures"}
]
},
{
"id": "2",
"title": "Performance and Accuracy Trade-offs",
"subsections": [
{"id": "2.1", "title": "Factual Accuracy and Hallucination Rates"},
{"id": "2.2", "title": "Latency and Throughput Benchmarks"}
]
}
],
"queries": [
{
"id": "q1",
"query": "RAG retrieval-augmented generation architecture components ...",
"target_sections": ["Architectural Foundations"],
"rationale": "Establishes baseline understanding of RAG pipelines"
}
]
}
This architecture has been tuned to perform well on both Deep Research Bench and Deep Research Bench II.
To customize the agent for your domain, edit the prompt templates in src/aiq_aira/agents/deep_researcher/prompts/
. For example, open planner.j2
and instruct the planner to keep outlines to three sections or fewer for more focused reports. You could also add additional debug logging to inspect the intermediate state (like /planner_output.md
) to see how your prompt changes affect the context passed between sub-agents.
Add a data source
The blueprint implements every tool as a NeMo Agent Toolkit function. To connect a new enterprise data source, implement a NeMo Agent Toolkit function and reference it in the config.
Step 1: Implement the NeMo Agent Toolkit function
The following example connects to an internal knowledge base API:
# sources/internal_kb/src/register.py
from pydantic import Field, SecretStr
from nat.builder.builder import Builder
from nat.builder.function_info import FunctionInfo
from nat.cli.register_workflow import register_function
from nat.data_models.function import FunctionBaseConfig
class InternalKBConfig(FunctionBaseConfig, name="internal_kb"):
"""Search tool for the internal knowledge base."""
api_url: str = Field(description="Knowledge base API endpoint")
api_key: SecretStr = Field(description="Authentication key")
max_results: int = Field(default=5)
@register_function(config_type=InternalKBConfig)
async def internal_kb(config: InternalKBConfig, builder: Builder):
async def search(query: str) -> str:
"""Search the internal knowledge base for relevant documents."""
results = await call_kb_api(config.api_url, query, config.max_results)
return format_results(results)
yield FunctionInfo.from_fn(search, description=search.__doc__)
NeMo Agent Toolkit validates the config fields at startup, so misconfigurations fail fast. The agent will use the function’s docstring to decide when to call the tool.
Step 2: Reference the tool in the config
Declare the new tool under functions
, then add it to each agent’s tools
list:
functions:
internal_kb_tool:
_type: internal_kb
api_url: "https://kb.internal.company.com/api/v1"
api_key: ${INTERNAL_KB_API_KEY}
max_results: 10
shallow_research_agent:
_type: shallow_research_agent
llm: nemotron_llm
tools:
- web_search_tool
- internal_kb_tool
deep_research_agent:
_type: deep_research_agent
orchestrator_llm: gpt-5
planner_llm: nemotron_llm
researcher_llm: nemotron_llm
tools:
- advanced_web_search_tool
- internal_kb_tool
You don’t need to change any agent code. The agent discovers the new tool’s name and description automatically, and the LLM calls it when a query matches. Use this same pattern to hook into your own enterprise systems or leverage MCP (Model Context Protocol) to grant your agents access to existing tools. This ensures your research stack remains private, and deeply integrated with the data that matters most to your organization.
Going further
By extending and building on the NVIDIA AI-Q blueprint, developers are able to bring a best-in-class LangChain deep agent architecture to their enterprise. To go further, review:
- Blueprint customization guide for adding more data sources
- Helm chart for deploying on an AI Factory
- Blueprint evaluation guide for doing evaluation driven development
- LangSmith for monitoring the system in production and preventing performance drift
The NVIDIA AI-Q Blueprint is being integrated by partners across the ecosystem, including: Aible, Amdocs, Cloudera, Cohesity, Dell, Distyl, H2O.ai, HPE, IBM, JFrog, LangChain, ServiceNow, and VAST.
