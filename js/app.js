app = new Vue({
    el: '#app',
    data: {
        selected_actor: null,
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
                        borderWidth: 1
                    }]
                },
                options: {
                    title: {
                        display: true,
                        text: '出演作品のタグ合計  (2020.01.15データ入手)',
                        fontSize: 18
                    },
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