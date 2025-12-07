local io = require("io")
local string = require("string")

local inputfile = arg[1] == "test" and "example.txt" or "input.txt"

local Counter = {}

function Counter:new()
  local o = { items = {} }
  setmetatable(o, self)
  self.__index = self
  return o
end

function Counter:increment(value, count)
  count = count or 1
  self.items[value] = (self.items[value] or 0) + count
end

function Counter:delete(value)
  self.items[value] = nil
end

function Counter:get(value)
  return self.items[value]
end

local function part_1()
  local beam_counters = Counter:new()
  local split_count = 0
  for line in io.lines(inputfile) do
    local start, _ = line:find("S", 1, true)
    if start then
      beam_counters:increment(start)
    end

    local splitter_idx = 0
    while true do
      splitter_idx, _ = line:find("^", splitter_idx + 1, true)
      if not splitter_idx then
        break
      end
      if beam_counters:get(splitter_idx) then
        split_count = split_count + 1
        beam_counters:delete(splitter_idx)
        if splitter_idx > 0 then
          beam_counters:increment(splitter_idx - 1)
        end
        if splitter_idx < line:len() then
          beam_counters:increment(splitter_idx + 1)
        end
      end
    end
  end
  return split_count
end

local function part_2()
  local beam_counters = Counter:new()
  local timelines = 1
  for line in io.lines(inputfile) do
    local start, _ = line:find("S", 1, true)
    if start then
      beam_counters:increment(start)
    end

    local splitter_idx = 0
    while true do
      splitter_idx, _ = line:find("^", splitter_idx + 1, true)
      if not splitter_idx then
        break
      end
      local beam_counts = beam_counters:get(splitter_idx)
      if beam_counts then
        timelines = timelines + beam_counts
        beam_counters:delete(splitter_idx)
        if splitter_idx > 0 then
          beam_counters:increment(splitter_idx - 1, beam_counts)
        end
        if splitter_idx < line:len() then
          beam_counters:increment(splitter_idx + 1, beam_counts)
        end
      end
    end
  end
  return timelines
end

local function main()
  local p1 = part_1()
  print(string.format("Part 1: %15d", p1))
  local p2 = part_2()
  print(string.format("Part 2: %15d", p2))
end

main()
