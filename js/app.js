app = new Vue({
    el: '#app',
    data: {
        selected_actor: 'そらまめ。',
        selected_tag: 'バイノーラル/ダミヘ',
        labels: basic_data['labels'],
        colors: basic_data['colors'],
        actors: basic_data['actors'],
        full_data: full_data,
        tag_chart: null,
        actor_chart: null
    },
    methods: {
        update_tag_chart: function () {
            this.tag_chart.destroy()
            this.create_tag_chart()
        },
        update_actor_chart: function () {
            this.actor_chart.destroy()
            this.create_actor_chart()
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
        sortList: function (dataList, labelList){
            argIndices = this.argsort(dataList)

            var sorted_dataList = []
            var sorted_labelList = []

            for (let index in argIndices){
                sorted_dataList.push(dataList[argIndices[index]]);
                sorted_labelList.push(labelList[argIndices[index]]);
            }

            return [sorted_dataList, sorted_labelList];
        },
        create_tag_chart: function () {
            if (!this.actors.includes(this.selected_actor)){
                sorted_data = [[], []]
            }else{
                var dataList = this.full_data[this.selected_actor]
                sorted_data = this.sortList(dataList, this.labels)
            }

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
        },
        create_actor_chart_dataList: function (){
            var index = this.labels.indexOf(this.selected_tag)

            var dataList = []
            for (let actor in this.full_data) {
                dataList.push(this.full_data[actor][index], )
            }

            return dataList
        },
        create_actor_chart: function () {
            if (!this.labels.includes(this.selected_tag)){
                sorted_data = [[], []]
            }else{
                var dataList = this.create_actor_chart_dataList()
                sorted_data = this.sortList(dataList, this.actors)
            }

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
                        text: 'あるタグがついた作品への出演合計  (2020.01.15データ入手)',
                        fontSize: 18
                    },
                    legend: {
                        display: false
                    },
                    maintainAspectRatio: false
                }
            };
            this.actor_chart = new Chart(document.getElementById('actor-chart').getContext('2d'), config);
        }
    },
    mounted: function () {
        this.create_actor_chart();
        this.create_tag_chart();
    }
})