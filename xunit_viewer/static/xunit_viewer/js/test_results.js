$(function() {
    var data = [
        {
            value: stats.errors,
            color:'#F7464A',
            label: 'Errors'
        },
        {
            value: stats.failures,
            color:'#F77446',
            label: 'Failures'
        },
        {
            value: stats.successful,
            color: '#46BFBD',
            label: 'Successful'
        },
        {
            value: 1,//stats.skipped,
            color: '#FDE4EC',
            label: 'Skipped'
        }
    ]

    var ctx = $('#pie_chart').get(0).getContext('2d');
    var myPieChart = new Chart(ctx).Pie(data);
});
