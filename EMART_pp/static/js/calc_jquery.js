var total = document.getElementById("total");
        var netPrice = document.getElementsByClassName("netPrice");
        function price(price) {
            var cal = 0;
            var amount = price.parentElement.parentElement.children[1].children[0].value;
            var res = price.parentElement.parentElement.children[2].innerHTML = amount * price.value;
            for (let i = 0; i < netPrice.length; i++) {
                cal += parseInt(netPrice[i].innerText);
            }
            total.innerHTML = cal;
        }
        function amount(amount) {
            var cal = 0;
            var price = amount.parentElement.parentElement.children[0].children[0].value;
            var res = amount.parentElement.parentElement.children[2].innerHTML = price * amount.value;
            for (let i = 0; i < netPrice.length; i++) {
                cal += parseInt(netPrice[i].innerText);
            }
            total.innerHTML = cal;
        }
