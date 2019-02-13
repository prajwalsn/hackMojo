var app = angular.module("myapp",[]);

app.config(['$interpolateProvider', function($interpolateProvider) {
    $interpolateProvider.startSymbol('{a');
    $interpolateProvider.endSymbol('a}');
  }]);
//controller for index page
app.controller("ctrl",['$scope','$http',function($scope,$http)
{
        
        $scope.videos = []
        $http.get("{{ url_for('/get_movie_names') ").then(function(response)
        {
          console.log(response);
          $scope.videos = response['data']['categories'];  
        },
        function(err)
        {
            console.log(err);
        });
}]);