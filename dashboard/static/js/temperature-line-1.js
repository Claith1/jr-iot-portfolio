var counter = 0
var lineDynamicUpdate = function() {
    let url = "http://192.168.1.14:5000/api/device-load"
    let method = "GET"
    let typeOfResponse = "json"

    let xhr = new XMLHttpRequest()
    xhr.open(method, url)
    xhr.responseType = typeOfResponse
    xhr.send()
    xhr.onload = function() {
        let responseObj = xhr.response

            myDynamicLineChart.data.labels.unshift(responseObj.created_at)
            myDynamicLineChart.data.datasets[0].data.unshift(responseObj.load)
            if (counter > 25) {
                myDynamicLineChart.data.labels.pop()
                myDynamicLineChart.data.datasets[0].data.pop()
            }
            myDynamicLineChart.update()
            counter++
    }
}

setInterval(lineDynamicUpdate, 5000);

var myDynamicLineChartCanvas = document.getElementById('Temp-Line-Canvas')
var lineData = {
    datasets: [{
        label: 'Current',
        data: [0],
        borderWidth: 2,
        lineTension: 0.2,
        //backgroundColor: [
        //   'rgba(24, 58, 55, 0.4)',
        //],
        borderColor: [
            'rgba(24, 58, 55, 1)',
        ],
    }],
}

var lineOptions = {
    legend: {
        display: false
    },
    title: {
        display: true,
        text: 'CPU Load'
    },
    scales: {
        xAxes: [{
            scaleLabel: {
                display: true,
                labelString: 'Time',
            },
        }],
        yAxes: [{
            scaleLabel: {
                display: true,
                labelString: 'Percentage',
            },
            ticks: {
                beginAtZero: true,
                suggestedMin: 0,
                suggestedMax: 100,
            },
        }],
    },
}

var myDynamicLineChart = new Chart(myDynamicLineChartCanvas, {
    type: 'line',
    data: lineData,
    options: lineOptions,
})