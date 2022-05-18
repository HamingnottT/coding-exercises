def thruRecursion(List, Low, High, target):
        if High >= Low:
            midpoint = (High + Low) // 2

            if List[midpoint] == target:
                return midpoint
            
            elif List[midpoint] > target:
                return thruRecursion(List, Low, midpoint - 1, target)

            else:
                return thruRecursion(List, midpoint + 1, High, target)

        else:
            return "not present, something else is going on"