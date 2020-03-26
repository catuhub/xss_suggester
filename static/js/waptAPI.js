const MAIN_ENDPOINT = "/wapt"

RESPONSE_CODE_OK = "0"


/**
 * waptCategories
 *
 * @returns  list of categories
 */
function waptCategories(cb) {
  $.get(MAIN_ENDPOINT,  function(data) {
    cb(null, data);
  });
}

function waptHackingGoals(category, cb) {
      $.get(MAIN_ENDPOINT + "/" + category, cb);
}

function waptSetHackingGoal(category, goal, returnCB) {
  var ret = {}
  async.waterfall([
    function(cb) {
      $.get(MAIN_ENDPOINT + "/" + category + "/" + goal, function(data) {
        cb(null, data);
      });
    },
    // Get observations
    function(retCode, cb) {
      console.log("ASK OBSERVATIONS");
      $.get(MAIN_ENDPOINT + "/ask/observations" , function(data) {
        console.log("Taken observations");
        cb(null, data);
      })
    },
    function(responseObs, cb) {
      ret['observations'] = JSON.parse(responseObs);
      $.get(MAIN_ENDPOINT + "/ask/actions", function(data) {
        console.log("Taken action");
        cb(null, data);
      })
    },
    function(responseActs, cb) {
      ret['actions'] = JSON.parse(responseActs);
      cb(null);
    }], function(err) {
    returnCB(ret);
  })
}

function waptAsk(category, goal, returnCB) {
    var ret = {}
    async.waterfall([
        // Get observations
        function(cb) {
            console.log("ASK OBSERVATIONS");
            $.get(MAIN_ENDPOINT + "/ask/observations" , function(data) {
                console.log("Taken observations");
                cb(null, data);
            })
        },
        function(responseObs, cb) {
            ret['observations'] = JSON.parse(responseObs);
            $.get(MAIN_ENDPOINT + "/ask/actions", function(data) {
                console.log("Taken action");
                cb(null, data);
            })
        },

        function(responseActs, cb) {
            ret['actions'] = JSON.parse(responseActs);
            $.get(MAIN_ENDPOINT + "/ask/finalstate", function(data) {
              ret['isFinalState'] = JSON.parse(data).isFinalState;
              cb(null);
            });
        }], function(err) {

        returnCB(ret);
    })
}

function waptSendObservation(observationId) {

  var deferred = $.Deferred();

  $.ajax({
      url: MAIN_ENDPOINT + '/tell/observation/' + observationId,
      method: 'PUT'
  })
      .then(function() {
          deferred.resolve();
      })
      .fail(function() {
        deferred.reject();
      })
  return deferred.promise();
}

function waptInit(returnCB) {
  var categories = []
  async.waterfall([
    function(cb) {
      waptCategories(cb);
    },
    function(cat, cb) {
      console.log(categories);
      categories = cat
      cb(null);
    }
  ], function() {
    returnCB(categories);
  });
}
