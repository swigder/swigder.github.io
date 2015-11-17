app.controller("wordSegmenterController", function ($scope, $http) {
    $scope.segment = function () {
        $http({
            method: 'GET',
            url: '/segment/' + $scope.sentence
        }).then(function successCallback(response) {
            $scope.segmented = response.data
        });
    };
});
