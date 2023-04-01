
//let form1;
//let form2={};




function submitForm() {
  const form = document.getElementById('myForm1');
  const formData = new FormData(form);
  const data = {};
  formData.forEach((value, key) => data[key] = value);
  const jsonData = JSON.stringify(data);
  console.log(jsonData)
  window.location.href = "coursecreditdetails.html";
  return jsonData; 
}




function submitForm2() {
  const form = document.getElementById('myForm2');
  const formData = new FormData(form);
  const data = {};
  formData.forEach((value, key) => data[key] = value);
  const jsonData = JSON.stringify(data);
  console.log(jsonData)
  window.location.href = "learningoutcomes.html";
  return jsonData; 
}


//console.log(form2);

//console.log(form1)

//console.log("test")