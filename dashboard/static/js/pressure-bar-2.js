var chartCanvas1 = document.getElementById('Pressure-Bar')
        var barData = {
            datasets: [{
                label: 'Current',
                data: [190.4],
                borderWidth: 1,
                backgroundColor: [
                    'rgba(67, 37, 52, 0.4)',
                ],
                borderColor: [
                    'rgba(67, 37, 52, 1)',
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