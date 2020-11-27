 var chartCanvas1 = document.getElementById('Humidity-Bar')
        var barData = {
            datasets: [{
                label: 'Current',
                data: [22.4],
                borderWidth: 1,
                backgroundColor: [
                    'rgba(4, 21, 31, 0.4)',
                ],
                borderColor: [
                    'rgba(4, 21, 31, 1)',
                ],
            }],
        }

        var barOptions = {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true,
                    },
                }],
            },
        }

        var myChart1 = new Chart(chartCanvas1, {
            type: 'bar',
            data: barData,
            options: barOptions,
        })