local io = require("io")
local math = require("math")
local string = require("string")
local table = require("table")

local inputfile = arg[1] == "test" and "example.txt" or "input.txt"
local COUNT = arg[1] == "test" and 10 or 1000

local Set = {}

function Set:new()
  local o = { items = {}, size = 0 }
  setmetatable(o, self)
  self.__index = self
  return o
end

function Set:insert(value)
  if not self.items[value] then
    self.items[value] = true
    self.size = self.size + 1
  end
end

function Set:intersects(set)
  for k1, _ in pairs(self.items) do
    for k2, _ in pairs(set.items) do
      if k1 == k2 then
        return true
      end
    end
  end
  return false
end

function Set:union(set)
  local res = Set:new()
  for key, _ in pairs(self.items) do
    res:insert(key)
  end
  for key, _ in pairs(set.items) do
    res:insert(key)
  end
  return res
end

function Set:remove(value)
  if self.items[value] then
    self.items[value] = nil
    self.size = self.size - 1
    return true
  end
  return false
end

function Set:contains(value)
  return self.items[value] or false
end

local function distance(boxes, i, j)
  local a = boxes[i]
  local b = boxes[j]
  return math.pow(a.x - b.x, 2) + math.pow(a.y - b.y, 2) + math.pow(a.z - b.z, 2)
end

local function get_boxes_and_pairs()
  local boxes = {}
  for line in io.lines(inputfile) do
    local x, y, z = line:match("(%d+),(%d+),(%d+)")
    boxes[#boxes + 1] = { x = tonumber(x), y = tonumber(y), z = tonumber(z) }
  end
  local pairs = {}
  for i = 2, #boxes do
    for j = 1, i - 1 do
      pairs[#pairs + 1] = { first = i, second = j }
    end
  end
  table.sort(pairs, function(a, b)
    return distance(boxes, a.first, a.second) < distance(boxes, b.first, b.second)
  end)
  return boxes, pairs
end

local function compute_circuits(a, b, circuits)
  local new = true
  local merge = 0
  local delete = 0
  for j, circuit in ipairs(circuits) do
    if new and (circuit:contains(a) or circuit:contains(b)) then
      circuit:insert(a)
      circuit:insert(b)
      merge = j
      new = false
    elseif not new and (circuit:contains(a) or circuit:contains(b)) then -- directly check for intersects
      circuits[#circuits + 1] = circuits[merge]:union(circuit)
      delete = j
      break
    end
  end
  if new then
    local circuit = Set:new()
    circuit:insert(a)
    circuit:insert(b)
    circuits[#circuits + 1] = circuit
  elseif delete > 0 then
    table.remove(circuits, merge)
    table.remove(circuits, delete - 1)
  end
end

local function part_1()
  local _, pairs = get_boxes_and_pairs()
  local circuits = {}
  for idx = 1, COUNT do
    local a = pairs[idx].first
    local b = pairs[idx].second
    compute_circuits(a, b, circuits)
  end
  table.sort(circuits, function(a, b)
    return a.size > b.size
  end)
  local product = 1
  for i = 1, 3 do
    product = product * circuits[i].size
  end
  return product
end

local function part_2()
  local boxes, pairs = get_boxes_and_pairs()
  local circuits = {}
  local idx = 0
  while #circuits ~= 1 or circuits[1].size ~= #boxes do
    idx = idx + 1
    local a = pairs[idx].first
    local b = pairs[idx].second
    compute_circuits(a, b, circuits)
  end
  return boxes[pairs[idx].first].x * boxes[pairs[idx].second].x
end

local function main()
  local p1 = part_1()
  print(string.format("Part 1: %15d", p1))
  local p2 = part_2()
  print(string.format("Part 2: %15d", p2))
end

main()
