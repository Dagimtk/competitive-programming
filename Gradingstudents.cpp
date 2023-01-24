vector<int> gradingStudents(vector<int> grades){
    int n;
    for(int i=0; i<grades.size(); i++){
    if(grades[i]>=38)
    {
     n=grades[i]%5;
     if(n>=3)
     grades[i]+=(5-n);
     
    }
    }
    return grades;

}
