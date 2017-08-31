var students = [ 
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
];

function printName(studentList)
{
	for (var i=0;i<studentList.length;i++)
	{
		var fullName = (studentList[i].first_name + " " + studentList[i].last_name);
		console.log(fullName);
	}
}

printName(students);