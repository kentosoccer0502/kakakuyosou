//let button = document.querySelector("#predict")
//button.addEventListener("click", function(){
//    let predicted_price = document.querySelector("#predicted-price")
//   predicted_price.innerHTML = "5000";
//});

const app = Vue.createApp({
    data: () => ({
        roomSize: 50,
        distance: 10,
        years: 20,
        area: "A",
        predictedPrice:0,
    }),
    methods:{
        predict(){
            this.predictedPrice = 50000;
        }
    }
})
app.mount("#app")
