pm.test("Body contains string",() => {
    pm.expect(pm.response.text()).to.include("customer_id");
});

pm.test("Body contains string",() => {
    pm.expect(pm.response.text()).to.include("This is the first responce from server!");
});

pm.test("Body is string", function () {
    pm.response.to.have.body("whole-body-text");
});

pm.test("Body is string", function () {
    pm.response.to.have.body("This is the first responce from server!");
});

pm.test("Body matches string", function () {
    pm.expect(pm.response.text()).to.include("string_you_want_to_search");
});

pm.test("Body matches string", function () {
    pm.expect(pm.response.text()).to.include("This is the first responce from server!");
});
