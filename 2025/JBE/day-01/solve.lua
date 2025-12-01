local io = require("io")
local math = require("math")

local inputfile = arg[1] == "test" and "example.txt" or "input.txt"

local function part_1()
  local dial = 50
  local res = 0
  for line in io.lines(inputfile) do
    local val = line:match("L(%d+)")
    if val then
      val = -tonumber(val)
    else
      val = tonumber(line:match("R(%d+)"))
    end
    dial = (dial + val) % 100
    if dial == 0 then
      res = res + 1
    end
  end
  return res
end

local function part_2()
  local dial = 50
  local res = 0
  for line in io.lines(inputfile) do
    local val = line:match("L(%d+)")
    if val then
      val = -tonumber(val)
    else
      val = tonumber(line:match("R(%d+)"))
    end
    assert(val, "should parse number")
    local rounds = math.floor(math.abs(val) / 100)
    res = res + rounds
    local rem = math.fmod(val, 100)
    local old = dial
    dial = dial + rem
    if old ~= 0 and (dial > 99 or dial < 1) then
      res = res + 1
    end
    dial = dial % 100
  end
  return res
end

local function main()
  local p1 = part_1()
  print("Part 1:", p1)
  local p2 = part_2()
  print("Part 2:", p2)
end

main()
