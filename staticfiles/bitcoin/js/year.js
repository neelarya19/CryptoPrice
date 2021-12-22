var endpoint='/api/year'
var defaultdata=[]
var l=[]
main_data=[]
$.ajax({
    method:"GET",
    url:endpoint,
    success: function(data){
        defaultdata=data.x
        l=data.y
        console.log(defaultdata)
        console.log(l)



        setChart()
        
        
    },
    error: function(error_data){
        console.log("error")
        console.log(error_data)
    }
});

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
                    unit:'month',
                }
            }
        }
    },
    });
};

            // data: [
            //     {x: '2021-09-23',y:12},
            //     {x: '2021-09-26',y:10.5},
            //     {x: '2021-09-28',y:10.5},
            //     {x:'2021-10-23',y:10.5},
            //     {x:'2021-10-26',y:10.5},
            //     {x:'2021-10-28',y:10.5},
            //     {x:'2021-11-20',y:10.5},
            //     {x:'2021-11-18',y:10.5},
            //     {x:'2021-12-02',y:10.5},
            //     {x:'2021-12-04',y:10.5},
            // ],

