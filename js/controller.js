app.controller("controller", function ($scope, $http) {
    $scope.segment = function () {
        $http({
            method: 'GET',
            url: '/segment/' + $scope.segmentSentence
        }).then(function successCallback(response) {
            $scope.segmented = response.data
        });
    };

    $scope.weasel = function () {
        $http({
            method: 'GET',
            url: '/weasel/' + $scope.weaselSentence
        }).then(function successCallback(response) {
            $scope.weaseled = response.data.data
        });
    };
});
