var endpoint='/api/week'
var defaultdata=[]
var l=[]
main_data=[]
$.ajax({
    method:"GET",
    url:endpoint,
    success: function(data){
        defaultdata=data.x
        l=data.y
        defaultdata.reverse()
        l.reverse()
        setChart()
        
        
    },
    error: function(error_data){
        console.log("error")
        console.log(error_data)
    }
})

function setChart(){
    var ctx = document.getElementById('myChart');
    var myChart = new Chart(ctx, {
    type: 'line',

    data: {
        labels: l,
        borderColor : "#000000",
        datasets: [{
            label: 'Price(In USD)',

            data:defaultdata,
            // backgroundColor: [
            //     'rgba(255,255,255)',
            // ],
            borderColor: 'rgba(31, 204, 77)',

            borderWidth:4,
            pointStyle:'line',
        }],
    },
    options: {
        scales: {
            x: {
                type:'time',
                time: {
                    unit:'day',
                }
            }
        }
    },
    });
}