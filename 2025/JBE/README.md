# JBE's Solutions to AOC 2025

These solutions use pure Lua, without any fancy libraries or anything. Since Lua is pretty
bare-bones and does not include lots of the niceties that other languages have in their standard
libraries, solutions can become slightly longer (e.g. table reductions and similar operations need
to be implemented manually). The solutions are written for Lua 5.1 (with LuaJIT extensions).

Run the solutions as follows within each directory:

```sh
# run on test input based on example.txt
luajit solve.lua test
# run on actual input based on input.txt
luajit solve.lua
```
