function validateLogin() {

    let countryId = document.getElementById("countryId");
    let stateId = document.getElementById("stateId");
    let ajax = new XMLHttpRequest();
    stateId.innerHTML = ""
    ajax.onreadystatechange = function () {
        if (ajax.readyState === 4) {
            console.log("country", countryId);
            console.log(ajax.responseText);
            let jsn = JSON.parse(ajax.responseText);
            console.log("json", jsn);

            console.log("--json[0]-->" + jsn[0])
            console.log("--json[1]-->" + jsn[1])

            for (let i = 0; i < jsn.length; i++) {
                let opt = document.createElement('option');
                opt.value = jsn[i]['stateId'];
                opt.text = jsn[i]['stateName'];
                stateId.options.add(opt);
            }
        }
    };
    ajax.open("get", "/validate_login?countryId=" + countryId.value, true);
    ajax.send();
}