// 1. Отправить запрос.
// 2. Статус код 200
// 3. Спарсить response body в json.
// 4. Проверить, что name в ответе равно name s request (name вбить руками.)
var resp = pm.response.json();
pm.test("Check name", function () {
        pm.expect(resp.name).to.eql("Mikhail");
});

// 5. Проверить, что age в ответе равно age s request (age вбить руками.)
pm.test("Check age", function(){
        pm.expect(resp.age).to.eql("39");
});

// 6. Проверить, что salary в ответе равно salary s request (salary вбить руками.)
pm.test("Check salary", function(){
        pm.expect(resp.salary).to.eql(2000)
});

// 7. Спарсить request.
var req_name = request.data.name
console.log("req_name = ", req_name)

var req_age = request.data.age
console.log("req_age = ", req_age)

var req_salary = +request.data.salary
console.log("req_salary = ", req_salary)

// 8. Проверить, что name в ответе равно name s request (name забрать из request.)
// 9. Проверить, что age в ответе равно age s request (age забрать из request.)
// 10. Проверить, что salary в ответе равно salary s request (salary забрать из request.)
pm.test("Check_req_name", function(){
    pm.expect(resp.name).to.eql(req_name);
});
pm.test("Check_req_age", function(){
    pm.expect(resp.age).to.eql(req_age);
});
pm.test("Check_req_age", function(){
    pm.expect(resp.salary).to.eql(req_salary);
});

// 11. Вывести в консоль параметр family из response.
var resp_fam = resp.family
console.log(resp_fam);

// 12. Проверить что u_salary_1_5_year в ответе равно salary*4 (salary забрать из request)
var u_salary_1_5_year = pm.response.json().family.u_salary_1_5_year;
console.log("u_salary_1_5_year = ", u_salary_1_5_year)

pm.test("u_salary_1_5_year", function(){
    pm.expect(u_salary_1_5_year).to.eql(req_salary*4);
});
console.log("u_salary_1_5_year = ", u_salary_1_5_year)
