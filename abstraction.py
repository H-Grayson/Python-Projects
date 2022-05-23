from abc import ABC, abstractmethod
class student(ABC):
    def studentGPAReq(self, total):
        print("The required GPA for math is ",total)

    @abstractmethod
    def mathGrade(self,total):
        pass

class graduationReq(student):
    def mathGrade(self, total):
        print('You meet the graduation requirement for Math!'.format(total))

obj = graduationReq()
obj.mathGrade("82")
