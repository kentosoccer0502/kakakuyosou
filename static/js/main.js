const app = Vue.createApp({
    data: () => ({
        terms:{
            roomSize: 50,
            distance: 10,
            years: 20,
            area: "A",
        },
        predictedPrice:0,
    }),
    methods:{
        predict(){
            this.predictedPrice = 50000;
        },
        predictWithoutTerms:function() {
            axios
                .get('/predict')
                .then((response) => {
                this.predictedPrice = response.data['predicted_price'];
            }
        ).catch((error) => {
            console.log(error);
            });
        },
        predictWithTerms:function() {
            axios
                .post('/predict', this.terms)
                .then((response) => {
                this.predictedPrice = response.data['predicted_price'];
            }
        ).catch((error) => {
            console.log(error);
            });
        },
    },
})
app.mount("#app")
