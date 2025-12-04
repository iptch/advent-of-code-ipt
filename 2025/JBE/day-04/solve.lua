local io = require("io")

local inputfile = arg[1] == "test" and "example.txt" or "input.txt"

local THRESHOLD = 4
local CHAR = "@"

local function get_grid()
  local grid = {}
  for line in io.lines(inputfile) do
    local row = {}
    for i = 1, line:len() do
      row[#row + 1] = line:sub(i, i)
    end
    grid[#grid + 1] = row
  end
  return grid
end

local function each(grid, func)
  local res = 0
  for i, row in ipairs(grid) do
    for j, val in ipairs(row) do
      if val == CHAR then
        local count = 0
        for x = -1, 1, 1 do
          for y = -1, 1, 1 do
            if grid[i + x] and grid[i + x][j + y] == CHAR then
              count = count + 1
            end
          end
        end
        res = res + func(count, i, j, grid)
      end
    end
  end
  return res
end

local function part_1()
  local grid = get_grid()
  return each(grid, function(count, _, _, _)
    return count <= THRESHOLD and 1 or 0
  end)
end

local function score(grid)
  local sum = 0
  for _, row in ipairs(grid) do
    for _, val in ipairs(row) do
      if val == CHAR then
        sum = sum + 1
      end
    end
  end
  return sum
end

local function part_2()
  local res = 0
  local grid = get_grid()
  local s = score(grid)
  while true do
    res = res
      + each(grid, function(count, i, j, g)
        if count <= THRESHOLD then
          g[i][j] = "."
          return 1
        else
          return 0
        end
      end)
    local t = score(grid)
    if s == t then
      return res
    end
    s = t
  end
end

local function main()
  local p1 = part_1()
  print("Part 1:", p1)
  local p2 = part_2()
  print("Part 2:", p2)
end

main()
