# /* Problem Name is &&& Snowpack &&& PLEASE DO NOT REMOVE THIS LINE. */

# /*
# ** Instructions to candidate.
# **  1) Given an array of non-negative integers representing the elevations
# **     from the vertical cross section of a range of hills, determine how
# **     many units of snow could be captured between the hills.
# **
# **     See the example array and elevation map below.
# **                                 ___
# **             ___                |   |        ___
# **            |   |        ___    |   |___    |   |
# **         ___|   |    ___|   |   |   |   |   |   |
# **     ___|___|___|___|___|___|___|___|___|___|___|___
# **     {0,  1,  3,  0,  1,  2,  0,  4,  2,  0,  3,  0}
# **                                 ___
# **             ___                |   |        ___
# **            |   | *   *  _*_  * |   |_*_  * |   |
# **         ___|   | *  _*_|   | * |   |   | * |   |
# **     ___|___|___|_*_|___|___|_*_|___|___|_*_|___|___
# **     {0,  1,  3,  0,  1,  2,  0,  4,  2,  0,  3,  0}
# **
# **     Solution: In this example 13 units of snow (*) could be captured.
# **
# **  2) Consider adding some additional tests in doTestsPass().
# **  3) Implement computeSnowpack() correctly.
# */

"""
# find left
    current should be greater than top

0, 1, 3, 0, 1, 1, 1, 4

"""
def get_bucket(arr):
    left, right = None, None
    stack = []
    i = 0

    while i < len(arr):
        if i == 0:
            stack.append(arr[i])
        else:
            if not left:
                if arr[i] > stack[-1]:
                    left = i
                else:
                    stack.pop()
                stack.append(arr[i])






# class Solution {
#   /*
#    **  Find the amount of snow that could be captured.
#    */
#   public static int computeSnowpack(int[] arr) {
#     // Todo: Implement computeSnowpack
#     return 0;
#   }

#   /*
#    **  Returns true if the tests pass. Otherwise, returns false;
#    */
#   public static boolean doTestsPass() {
#     boolean result = true;
#     result &= computeSnowpack(new int[] {0, 1, 3, 0, 1, 2, 0, 4, 2, 0, 3, 0}) == 13;

#     return result;
#   }

#   /*
#    **  Execution entry point.
#    */
#   public static void main(String[] args) {
#     if (doTestsPass()) {
#       System.out.println("All tests pass");
#     } else {
#       System.out.println("Tests fail.");
#     }
#   }
# }

