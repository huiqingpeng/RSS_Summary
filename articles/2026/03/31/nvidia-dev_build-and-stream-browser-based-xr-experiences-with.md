---
title: "Build and Stream Browser-Based XR Experiences with NVIDIA CloudXR.js"
source: "NVIDIA Developer Blog"
url: "https://developer.nvidia.com/blog/build-and-stream-browser-based-xr-experiences-with-nvidia-cloudxr-js/"
published: "2026-03-31"
fetched: "2026-04-01T07:14:21.683366"
---

Delivering high-fidelity VR and AR experiences to enterprise users has typically required native application development, custom device management, and complex deployment pipelines. Now, with the new JavaScript SDK NVIDIA CloudXR.js, developers can stream GPU-rendered immersive content directly to a standard web browser—no app store, no installs, no device-specific builds.
NVIDIA CloudXR.js brings the full power of NVIDIA RTX remote rendering to the web platform. This is a fundamental shift in how immersive applications are built and delivered. NVIDIA CloudXR.js expands access to enterprise XR beyond native development workflows and into the broad web developer community.
Developers building digital twins in NVIDIA Omniverse, robot teleoperation systems, or interactive 3D training environments can now reach users on XR headsets through a URL. This post walks through the SDK architecture, its core API, and how to connect it to server applications such as Omniverse, NVIDIA Isaac Lab, and LÖVR.
How to run and host an NVIDIA CloudXR.js client
This section explains how to run and host an NVIDIA CloudXR.js web client, including prerequisites and an architecture overview.
Prerequisites
To run and host a CloudXR.js-based web client, you need a computer with Node.js v20 or higher and npm installed. Check out the NVIDIA CloudXR.js Sample Client to try it without building the web client. You will still need an NVIDIA CloudXR server running CloudXR Runtime and an OpenXR-compatible app. Prerequisites include:
- Client side
- Node.js v20 or higher and npm
- A WebGL2 and WebXR-compatible browser (for example, Meta Quest Browser or Pico Browser on headsets, or any browser that runs an emulator)
- Familiarity with JavaScript/TypeScript and basic WebGL concepts
- A Meta Quest 2/3/3s (OS v79+) or Pico 4 Ultra (Pico OS 15.4.4U+) for headset testing
- Server side
- An NVIDIA GPU-equipped server with the latest requirements running NVIDIA CloudXR Runtime
- An OpenXR-compatible server application such as Omniverse, Isaac Lab, or LÖVR
- WiFi 6 or 6E network with <20 ms latency and 100+ Mbps bandwidth are highly recommended
CloudXR.js architecture
CloudXR.js uses a two-tier connection model that separates web application hosting from the XR streaming pipeline (Figure 1).
Client web server: A standard Node.js development server (or any static hosting solution) serves the web application to client devices over HTTP or HTTPS.
CloudXR Runtime connection: The SDK establishes a WebSocket connection from the browser to the CloudXR Runtime running on the server. This channel carries the WebRTC-based video stream, pose tracking data, and controller/hand input.
On the server side, the CloudXR Runtime pairs with any OpenXR-compatible application. It captures rendered stereo frames, encodes them using hardware-accelerated AV1, H.265, or H.264, and streams them to the client. The client decodes the video, composites it into the WebXR framebuffer, and sends tracking data back to the server, closing the loop at up to 120 frames per second.
The web application itself is framework agnostic. CloudXR.js integrates with vanilla WebGL, React Three Fiber, or any other WebXR-compatible library.
Install the SDK
To add CloudXR.js to a project, download the SDK from NVIDIA NGC. Then import it into your project.
npm install </path/to/sdk/nvidia-cloudxr-version.tar.gz>
The package includes TypeScript type definitions, so IDE autocompletion and type checking work out of the box. Execute this on a standard webpage.
Create a streaming session
The entire SDK surface centers on a single entry point: createSession
. Import it, configure the connection and rendering parameters, and pass optional delegate callbacks to handle lifecycle events. The following code snippet is for the core pieces around using the createSession
API.
// Basic session creation
const session = createSession({
serverAddress: '192.168.1.100',
serverPort: 49100,
useSecureConnection: false,
perEyeWidth: 2048,
perEyeHeight: 1792,
// from WebGl API
gl: webglContext,
// from WebXR API
referenceSpace: xrReferenceSpace
});
// With event delegates
const session = createSession(sessionOptions, {
onStreamStarted: () => {
console.info('CloudXR streaming started');
},
onStreamStopped: (error) => {
if (error) {
console.error('Streaming error:', error);
} else {
console.info('Streaming stopped normally');
}
}
});
// Connect to CloudXR Runtime
if (session.connect()) {
console.info('Connection initiated');
}
The perEyeWidth
and perEyeHeight
values (which must be multiples of 16) define the resolution of each eye’s view. The SDK automatically derives the full stream resolution from these values.
Integrate the render loop
Once connected, drive the streaming pipeline from your WebXR render loop. Each frame requires two calls: send the current tracking state to the server, then render the received frame.
function onXRFrame(time: number, frame: XRFrame) {
// Send head pose, controllers, and hand tracking to the server
session.sendTrackingStateToServer(time, frame);
// Render the streamed frame into the WebXR layer
session.render(time, frame, xrSession.renderState.baseLayer);
// Continue the loop
xrSession.requestAnimationFrame(onXRFrame);
}
xrSession.requestAnimationFrame(onXRFrame);
The sendTrackingStateToServer
method automatically captures and transmits controller button presses, trigger values, controller poses, hand tracking data (when supported by the device), and the viewer’s head pose. The server uses this data to render the next frame from the correct viewpoint with the correct input state. The render
method then composites the decoded video into the XR display.
Explore sample clients
CloudXR.js offers two sample clients that demonstrate different integration approaches.
WebGL sample
The WebGL sample (simple/
) provides a minimal, single-file TypeScript implementation that works directly with the WebXR and WebGL2 APIs. It includes a connection configuration UI, browser capability checks, and a straightforward render loop. This is the fastest path to understanding how CloudXR.js works under the hood.
React sample
The React sample (react/
) demonstrates a production-style architecture using React Three Fiber, React Three XR, and React Three UIKit. It features component-based session management, a dual UI system (2D HTML for configuration and 3D in-VR panels for interaction), and WebGL state tracking to prevent rendering conflicts between React Three Fiber and CloudXR.
Both samples support Docker deployment for quick testing:
# WebGL sample
docker build -t cloudxr-js-sample --build-arg EXAMPLE_NAME=simple .
docker run -d --name cloudxr-js-sample -p 8080:80 -p 8443:443 cloudxr-js-sample
# React sample
docker build -t cloudxr-react-sample --build-arg EXAMPLE_NAME=react .
docker run -d --name cloudxr-react-sample -p 8080:80 -p 8443:443 cloudxr-react-sample
For local development with hot reloading, install dependencies and start the dev server:
cd simple # or react
npm install </path/to/sdk/tarball.tar.gz
npm run dev-server
Navigate to http://localhost:8080 in your browser. On desktop, the Immersive Web Emulator Runtime (IWER) automatically loads to emulate a Meta Quest 3, so you can develop and test without a physical headset.
Connect to server applications
CloudXR.js works with any OpenXR-compatible application running alongside the CloudXR Runtime. The following three examples demonstrate the breadth of what you can stream: NVIDIA Omniverse, NVIDIA Isaac Lab, and LÖVR.
NVIDIA Omniverse
Stream high-fidelity USD digital twin scenes to XR headsets for architecture walkthroughs, design reviews, and industrial training. Omniverse Kit SDK 109.0.2 and later includes an integrated CloudXR WebRTC runtime, so the streaming pipeline is built directly into the platform. Operators interact with 3D content using hand tracking for direct manipulation within the streamed environment.
NVIDIA Isaac Lab
Build teleoperation workflows for dexterous robots. An operator wearing a Quest 2/3/3s or Pico 4 Ultra sees a real-time stereo rendering of the robot simulation and uses hand tracking to control the robot. Isaac Lab runs on Linux with Docker and the NVIDIA Container Toolkit, supporting dual-GPU configurations for maximum performance. For details, see Setting up CloudXR Teleoperation.
LÖVR
LÖVR is a lightweight, open source Lua-based VR framework that provides a simple path to a working server. Launch LÖVR with the --webrtc
flag and connect a CloudXR.js client. This is ideal for rapid prototyping and testing your client setup. Visit NVIDIA/cloudxr-lovr-sample on GitHub to get started.
Configure networking toward production
For production deployments or HTTPS hosting, set up a WebSocket proxy with TLS termination. CloudXR.js includes a sample for Docker-based HAProxy configuration that handles this automatically:
cd proxy
docker build -t cloudxr-wss-proxy .
docker run -d --name wss-proxy --network host \
-e BACKEND_HOST=localhost \
-e BACKEND_PORT=49100 \
-e PROXY_PORT=48322 \
cloudxr-wss-proxy
The proxy generates self-signed certificates, connects to the CloudXR Runtime on port 49100, and listens for secure WebSocket connections on port 48322. For enterprise Kubernetes deployments, the SDK documentation includes an NGINX Ingress configuration that supports multiple CloudXR servers with load balancing.
Ensure your firewall allows TCP port 49100 (signaling), UDP port 47998 (media streaming), and TCP port 48322 (WSS proxy, if using HTTPS).
Get started with CloudXR.js
NVIDIA CloudXR.js brings enterprise XR streaming to the web platform—GPU-rendered immersive content delivered through a URL, with no native app required. The SDK provides a clean, minimal API that integrates with any WebXR-compatible framework and supports multiple server applications, from Omniverse digital twins to Isaac Lab robot teleoperation. It includes the networking and performance tooling needed for production deployments.
By providing every web developer the tools to build and ship immersive experiences without the overhead of native XR development, CloudXR.js makes possible entirely new categories of applications. We’re excited to see what the developer community builds with this new SDK.
Download CloudXR.js and try the sample clients. For the fastest path to a working demo, start with the LÖVR sample server and the WebGL client. For the complete API reference, configuration guides, and deployment documentation, visit the CloudXR.js SDK documentation.
