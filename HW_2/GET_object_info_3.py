// 1. Отправить запрос.
// 2. Статус код 200
// 3. Спарсить response body в json.
var resp_json = pm.response.json();
console.log("resp_json = ", resp_json)

// 4. Спарсить request.
var req = pm.request.url.query.toObject();
console.log("req = ", req)

// 5. Проверить, что name в ответе равно name s request (name забрать из request.)
var req_name = pm.request.url.query.toObject().name;
console.log("req_name = ", req_name)

pm.test("Check_name", function (){
    pm.expect(resp_json.name).to.eql(req_name)
})
console.log("resp_json.name", resp_json.name, "=", req_name, "req_name")

// 6. Проверить, что age в ответе равно age s request (age забрать из request.)
var req_age = pm.request.url.query.toObject().age;
console.log("req_age = ", req_age)

pm.test("Check_age", function (){
    pm.expect(resp_json.age).to.eql(req_age)
})
console.log("age_response", resp_json.age, "=", req_age, "age_request")

// 7. Проверить, что salary в ответе равно salary s request (salary забрать из request.)
pm.test("Check_salary", function (){
    pm.expect(resp_json.salary).to.eql(+pm.request.url.query.toObject().salary);
});
console.log("salary_response", resp_json.salary, "=", pm.request.url.query.toObject().salary, "salary_request")

// 8. Вывести в консоль параметр family из response.
console.log("family_from_response = ", resp_json.family)

// 9. Проверить, что у параметра dog есть параметры name.
// 10. Проверить, что у параметра dog есть параметры age.
var resp_dog = pm.response.json().family.pets.dog
console.log(resp_dog)

pm.test("The_dog_has_parameters_name&age", () => {
  pm.expect(resp_dog).to.have.property("name");
  pm.expect(resp_dog).to.have.property("age");
});

var resp_dog_name = pm.response.json().family.pets.dog.name
console.log(resp_dog_name)

// 11. Проверить, что параметр name имеет значение Luky.
pm.test("Check_param_dog_name", () => {
    pm.expect(resp_dog_name).to.eql("Luky");
});
console.log("dog_name = "+resp_dog_name)

// 12. Проверить, что параметр age имеет значение 4.
var resp_dog_age = pm.response.json().family.pets.dog.age
console.log(resp_dog_age)

pm.test("Check_param_dog_age", () => {
    pm.expect(resp_dog_age).to.eql(4);
});
console.log("dog_age = "+resp_dog_age)
