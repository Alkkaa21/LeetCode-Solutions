from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students=deque(students)
        rotations=0
        while students:
            if students[0]==sandwiches[0]:
                sandwiches.pop(0)
                students.popleft()
                rotations=0
            else:
                stud=students.popleft()
                students.append(stud)
                rotations+=1
            if rotations==len(students):
                break
        return len(students)