app = new Vue({
    el: '#app',
    data: {
        selected_actor: "小石川うに",
        labels: basic_data["labels"],
        colors: basic_data["colors"],
        actors: basic_data['actors'],
        full_data: full_data,
        tag_chart: null
    },
    methods: {
        update_chart: function () {
            this.tag_chart.destroy()
            this.create_chart()
        },
        create_chart: function () {
            var dataList = this.full_data[this.selected_actor]

            config = {
                type: 'pie',
                data: {
                    labels: this.labels,
                    datasets: [{
                        backgroundColor: this.colors,
                        data: dataList,
                        borderWidth: 0
                    }]
                },
                options: {
                    legend: {
                        display: false
                    },
                    maintainAspectRatio: false
                }
            };
            this.tag_chart = new Chart(document.getElementById('tag-chart').getContext('2d'), config);
        }
    },
    mounted: function () {
        this.create_chart()
    }
})