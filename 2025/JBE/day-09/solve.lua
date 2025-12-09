local io = require("io")
local math = require("math")
local string = require("string")

local inputfile = arg[1] == "test" and "example.txt" or "input.txt"

local function part_1()
  local corners = {}
  for line in io.lines(inputfile) do
    local x, y = line:match("(%d+),(%d+)")
    corners[#corners + 1] = { x = tonumber(x), y = tonumber(y) }
  end
  local max = 0
  for _, c1 in ipairs(corners) do
    for _, c2 in ipairs(corners) do
      local size = (math.abs(c1.x - c2.x) + 1) * (math.abs(c1.y - c2.y) + 1)
      if size > max then
        max = size
      end
    end
  end
  return max
end

local function intersects(p1, p2, c1, c2)
  local x1 = math.min(c1.x, c2.x)
  local y1 = math.min(c1.y, c2.y)
  local x2 = math.max(c1.x, c2.x)
  local y2 = math.max(c1.y, c2.y)
  if p1.x == p2.x and (x1 < p1.x and p1.x < x2) then
    return not ((p1.y <= y1 and p2.y <= y1) or (p1.y >= y2 and p2.y >= y2))
  end
  if p1.y == p2.y and (y1 < p1.y and p1.y < y2) then
    return not ((p1.x <= x1 and p2.x <= x1) or (p1.x >= x2 and p2.x >= x2))
  end
  return false
end

local function part_2()
  local corners = {}
  for line in io.lines(inputfile) do
    local x, y = line:match("(%d+),(%d+)")
    corners[#corners + 1] = { x = tonumber(x), y = tonumber(y) }
  end
  local max = 0
  for i, c1 in ipairs(corners) do
    for j, c2 in ipairs(corners) do
      if i % 2 == j % 2 then
        local size = (math.abs(c1.x - c2.x) + 1) * (math.abs(c1.y - c2.y) + 1)
        if size > max then
          local contained = false
          for idx = 1, #corners - 1 do
            if intersects(corners[idx], corners[idx + 1], c1, c2) then
              contained = true
              break
            end
          end
          if not contained then
            max = size
          end
        end
      end
    end
  end
  return max
end

local function main()
  local p1 = part_1()
  print(string.format("Part 1: %15d", p1))
  local p2 = part_2()
  print(string.format("Part 2: %15d", p2))
end

main()
