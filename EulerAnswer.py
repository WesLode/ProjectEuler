from EulerAnswer_1to10 import EulerQuestionPt1

def EulerQuestion(question):
    if question <= 0:
        print('You have entered an invalid value :(')
        return 'boooooo'
    if question <=10 and question >0:
        final = EulerQuestionPt1(question)
        return final
