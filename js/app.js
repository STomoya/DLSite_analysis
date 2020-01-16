app = new Vue({
    el: '#app',
    data: {
        selected_actor: 'そらまめ。',
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
        argsort: function (array) {
            const arrayObject = array.map((value, idx) => { return { value, idx }; });
            arrayObject.sort((a, b) => {
                if (a.value > b.value) {
                    return -1;
                }
                if (a.value < b.value) {
                    return 1;
                }
                return 0;
            });
            const argIndices = arrayObject.map(data => data.idx);
            return argIndices;
        },
        sortList: function (dataList){
            argIndices = this.argsort(dataList)

            var sorted_dataList = []
            var sorted_labelList = []

            for (let index in argIndices){
                sorted_dataList.push(dataList[argIndices[index]]);
                sorted_labelList.push(this.labels[argIndices[index]]);
            }

            return [sorted_dataList, sorted_labelList];
        },
        create_chart: function () {
            var dataList = this.full_data[this.selected_actor]

            sorted_data = this.sortList(dataList)

            config = {
                type: 'pie',
                data: {
                    labels: sorted_data[1],
                    datasets: [{
                        backgroundColor: this.colors,
                        data: sorted_data[0],
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