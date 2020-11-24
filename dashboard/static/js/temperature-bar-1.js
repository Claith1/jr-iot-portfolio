

var chartCanvas1 = document.getElementById('Temperature-Bar')
        var barData = {
            datasets: [{
                label: 'Current',
                data: [35.6],
                borderWidth: 1,
                backgroundColor: [
                    'rgba(24, 58, 55, 0.4)',
                ],
                borderColor: [
                    'rgba(24, 58, 55, 1)',
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