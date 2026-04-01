---
title: "CUDA Tile Programming Now Available for BASIC!"
source: "NVIDIA Developer Blog"
url: "https://developer.nvidia.com/blog/cuda-tile-programming-now-available-for-basic/"
published: "2026-04-01"
fetched: "2026-04-02T07:08:10.851609"
---

CUDA 13.1 introduced CUDA Tile, a next generation tile-based GPU programming paradigm designed to make fine-grained parallelism more accessible and flexible. One of its key strengths is language openness: any programming language can target CUDA Tile, enabling developers to bring tile-based GPU acceleration into a wide range of ecosystems.
In response to overwhelming demand from seasoned developers everywhere, we’re releasing cuTile BASIC for GPUs, bringing CUDA Tile programming to this long-overlooked language.
What is cuTile BASIC?
cuTile BASIC is an expression of the CUDA Tile programming model in BASIC, built on top of the CUDA Tile IR specification. It enables you to write tile kernels in BASIC using a tile-based model, which is a natural fit for a programming language like BASIC which predates multi-threaded programming.
cuTile BASIC is the perfect marriage of the power of GPUs with the anachronistic charm and syntactic simplicity of the BASIC programming language – an elegant language, from a more pixelated era. Manually numbering your lines of code never looked so good or ran so fast!
Who is cuTile BASIC for?
BASIC is one of the oldest programming languages around and as such, is revered by a whole generation of developers who remember the sound of a 300 baud dial-up modem handshaking fondly. For many such developers, BASIC was their first introduction to computer programming.
Now, developers with BASIC still burned into their brains can take legacy applications onto NVIDIA GPU-accelerated computing for the first time. This unlocks performance and functionality the BASIC programming language could never have previously imagined – allowing your Lunar Lander to zip around the moon’s surface faster than an Artemis mission.
Relive the glory of writing games for your graphing calculator during math class while running on the world’s most powerful GPUs.
Get setup
First, install cuTile BASIC with PIP:
pip install git+https://github.com/nvidia/cuda-tile.git@basic-experimental
The full hardware and software requirements for running cuTile BASIC are listed at the end of this post (64k of RAM or more recommended).
cuTile BASIC example
If you’ve learned CUDA C++, you probably encountered the canonical vector addition kernel. A vector add kernel in CUDA C++ looks something like the following, which takes two vectors and adds them together elementwise to produce a third vector.
This is one of the simplest CUDA kernels one can write:
__global__ void vecAdd(float* A, float* B, float* C, int vectorLength)
{
/* calculate my thread index */
int workIndex = threadIdx.x + blockIdx.x*blockDim.x;
if(workIndex < vectorLength)
{
/* perform the vector addition */
C[workIndex] = A[workIndex] + B[workIndex];
}
}
In this kernel, each thread’s work is explicitly specified, and the programmer, when launching this kernel, will specify the number of blocks and threads to be launched.
Now let’s look at the equivalent code written in cuTile BASIC. We don’t need to specify what each thread does. We only have to break the data into tiles and specify what mathematical operations should happen to these tiles. Everything else is handled for us.
The cuTile BASIC vector add kernel is shown below:
10 REM Vector Add: C = A + B
20 INPUT N, A(), B()
30 DIM A(N), B(N), C(N)
40 TILE A(128), B(128), C(128)
50 LET C(BID) = A(BID) + B(BID)
60 OUTPUT C
70 END
This example is very basic and uses standard BASIC with three additional things to point out:
- Indexing an array returns a tile, which is a subset of the array.
- BID is a built-in variable that specifies the tile block index.
- TILE specifies what size tiles the arrays should be partitioned into.
Notice we didn’t have to specify anything other than the addition operation. Everything else is handled by cuTile BASIC.
Putting it all together
Now we’ll show how to run this vector add kernel in BASIC. The straightforward workflow is that first the BASIC function is compiled to a cubin, and then it’s launched on the GPU. For brevity, we’ve omitted the boring Python host and wrapper code, but you can find it in our GitHub repository.
If you have the proper versions of CUDA Toolkit and Python installed and have downloaded the cuTile BASIC repo from GitHub, you can execute the following command:
$ python examples/vector_add.py
[1/2] Compiling to cubin ...
Arrays: ['A', 'B', 'C'], tile_shapes={'A': [128], 'B': [128], 'C': [128]}, grid_size=8
[2/2] Launching kernel on GPU ...
Results (showing 5 samples of 1024):
C[ 0] = 0.0 (expected 0.0)
C[ 1] = 3.0 (expected 3.0)
C[ 511] = 1533.0 (expected 1533.0)
C[ 512] = 1536.0 (expected 1536.0)
C[1023] = 3069.0 (expected 3069.0)
VERIFICATION PASSED (max_diff=0.000000, 1024 elements)
If your output looks the same, congratulations, you just ran your very first cuTile BASIC program, and quite possibly your very first program of any sort written in BASIC! Max Headroom would be proud.
A BASIC matrix multiplication
BASIC is a simple language such that very few lines of code can express common algorithms. Consider a matrix multiply (GEMM) kernel in BASIC, shown below:
10 REM GEMM: C(M,N) = A(M,K) * B(K,N)
15 INPUT M, N, K, A(), B()
20 DIM A(M, K), B(K, N), C(M, N)
30 TILE A(128, 32), B(32, 128), C(128, 128), ACC(128, 128)
40 LET TILEM = INT(BID / INT(N / 128))
50 LET TILEN = BID MOD INT(N / 128)
60 LET ACC = 0.0
70 FOR KI = 0 TO INT(K / 32) - 1
80 LET ACC = MMA(A(TILEM, KI), B(KI, TILEN), ACC)
90 NEXT KI
100 LET C(TILEM, TILEN) = ACC
110 OUTPUT C
120 END
In this kernel, in addition to standard BASIC syntax, TILE
specifies how A, B, and C should be tiled and the size of the accumulator tile, ACC
. MMA
is the function call for matrix multiply and accumulate. Notice how simple this code is. You specify how your data should be subdivided into tiles, and specify your algorithm at a high-level, and under the covers, CUDA Tile handles everything else.
This example is also available in the GitHub repo’s examples folder. Running it produces the following output:
$ python examples/gemm.py
[1/2] Compiling to cubin ...
M=512, N=512, K=512, tile_shapes={'A': [128, 32], 'B': [32, 128], 'C': [128, 128]}, grid_size=16
[2/2] Launching kernel on GPU ...
Results (showing 5 samples of 512x512 = 262144 elements):
C[0,0] = -0.1199 (expected -0.1199)
C[0,1] = -14.4456 (expected -14.4456)
C[256,0] = -15.8891 (expected -15.8891)
C[256,1] = -2.8646 (expected -2.8646)
C[511,511] = 11.4724 (expected 11.4724)
VERIFICATION PASSED (max_diff=0.000012, tol=0.005120)
Matrix multiplication, such as that shown above, is at the heart of artificial intelligence tools like large language models. With cuTile Basic, developers can now explore the frontiers of artificial intelligence in models with trillions of parameters from a language that could barely imagine a whole megabyte of system memory.
How developers can get cuTile
To run cuTile BASIC programs, you need the following:
- A GPU with compute capability 8.x, 10.x, 11.x or 12.x (in future CUDA releases we’ll add support for additional GPU architectures)
- NVIDIA Driver R580 or later (R590 is required for tile-specific developer tools support)
- CUDA Toolkit 13.1 or later
- Python version 3.10 or higher
- cuTile BASIC package
Get started
Once you’ve got all the software, check out the full cuTile BASIC documentation, try all the sample programs found on GitHub, and start programming in cuTile BASIC today. Relish in the opportunity to port your modern AI or scientific computing code base to a historically pivotal language while retaining the ability to run on the most powerful hardware available! Just don’t tell your Commodore 64.
CUDA Tile in any language
While BASIC may not be the first language developers think of for high-performance parallel computing, it is an instructive demonstration that, thanks to the design of the CUDA software stack, CUDA Tile could be used from nearly any programming language. By compiling to the CUDA Tile IR format, CUDA Tile can be brought to just about any language … even BASIC!
Editor’s Note: In retrospect, developers asking for broad support of the CUDA Tile programming model should perhaps have been a bit more specific. Look for cuTile COBOL coming April 1, 2027.
