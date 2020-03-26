/******** GLOBALS **********/
// Current step
step=0;

/******** GLOBALS **********/

UI_NAMECATEGORY = "categoryRadio";
UI_NAMEHACKINGGOAL = "goalRadio";
UI_ELEMENT = '<div class="form-check">' +
  '<input class="form-check-input" type="radio" name="'+ UI_NAMECATEGORY +'" id="exampleRadios1" value="NoErrors"> '+
  '<label class="form-check-label" for="exampleRadios1"> ' +
  ' One selection '  +
  ' </label> ' +
  ' </div>';

var HackingGoal = {
  cat : "",
  hg : ""
}

/**
 * _getChecked
 *
 * @param element
 * @returns Checked element, -1 otherwise
 */
function _getChecked(element) {
  var ret= -1
  uiElement = $("input[name='"+ element  +"'");
  _.each(uiElement, function(e) {
    if (e.checked) {
      ret = e
    }
  })
  return ret
}
/**
 * buildCategoryPanel
 * Build a category panel
 * @param nameCategory : the name of the category
 * @param elements : the list of elements
 * @returns
 */
function UI_buildCategoryPanel(nameCategory, elements, name) {
  categoryElement = $(nameCategory);
  _.each(elements, function(hg) {
    console.log("in build category panel");
    var newEle = $(UI_ELEMENT).clone();
    var label = $(newEle).children("label");
    var input = $(newEle).children("input");
    input.attr('id', hg);
    input.attr('value', hg);
    input.attr('name', name)
    label.text(hg);
    categoryElement.append(newEle);
  });
}

function UI_categoryClicked(event) {
  console.log("Category clicked");
  var checked = _getChecked(UI_NAMECATEGORY);
  // No selected
  if (checked == -1) {
    UI_warnUser("Pls select a category");
  } else {
    var cat = checked.value;
    HackingGoal.cat = cat;
    waptHackingGoals(cat, function(data) {
      var obj = JSON.parse(data)
      var hgoals = obj.goals;
      UI_buildCategoryPanel("#hackinglist_body", hgoals, UI_NAMEHACKINGGOAL);
      $('#category-selection').show();
    });
  }

  // if(document.getElementById('exampleRadios1').checked) {
  //       $('#category-selection').show();
  //     }
  // });
};

function  UI_hackingGoalClicked(event) {
    var checked = _getChecked(UI_NAMEHACKINGGOAL);
    var hack = checked.value;
    HackingGoal.hg = hack;
    if (HackingGoal.hg && HackingGoal.cat) {
      waptSetHackingGoal(HackingGoal.cat, HackingGoal.hg, function(ret) {

        console.log(ret);

        initStep(normalizeActions(ret.actions.actions), normalizeObservations(ret.observations.observations));

      });

    $('#second_tab').children('.accordionjs-select').attr('checked','checked');
    } else {
      console.log("ERROR not defined");
      console.log(HackingGoal.hg);
      console.log(HackingGoal.cat);
    }
}





/************ STEPS GENERATION ***************/
function initStep (actionsArray, observationsArray) {
  step++;
  var accordionContent = $("#firstDiv");
  console.log(accordionContent);

    var html = '<div class="container-fluid" id="step'+step+'"><div class="separator-top"><button type="button" class="btn btn-danger" style="margin-bottom: -2px;">Step <span class="badge badge-light" style="font-size:1em">'+step+'</span></button></div>';
    html += '<h3>Suggestion:</h3>';
    html += '<div class="row" id="actions-step-'+step+'"></div>';
    html += '<h3>WHAT HAVE YOU OBSERVED?</h3>';
    html += '<div class="row observation-container" id="observations-step-'+step+'"></div>';
    html += '<hr>';
    html += '<div class="row justify-content-center"><div class="col-2">' +
        '<button id="report-btn" class="btn btn-primary submit-step-btn" data-step="'+step+'">Send</button>' +
        '<button id="select-category" class="btn btn-light">Reset</button></div></div>';

    accordionContent.append(html);

    $("#actions-step-"+step).append(generateActionsHtml(step, actionsArray));

    $("#observations-step-"+step).on('click','.ob-area', function(event) {
        $(this).addClass('active');
        $('.ob-area').not(this).removeClass('active')
        $(this).addClass('icon-show');
        $('.ob-area').not(this).removeClass('icon-show')
    });

    $("#observations-step-"+step).append(generateObservationsHtml(step, observationsArray));
}

function generateActionsHtml(step, actionsArray) {
    actionsArray = actionsArray.sort(function(a, b) {return parseFloat(b.reward) - parseFloat(a.reward)});
    console.log(actionsArray);

    var html = '';

    actionsArray.forEach(function(action) {
        var toReturn = '<div class="col-md-4">' +
        '<div class="card mb-4 shadow-sm">' +
        '<div class="card-header">REWARD: '+action.reward+'</div>' +
        '<div class="card-body">';

        action.subActions
            .filter(function(subAction) {
                return subAction.name !== "";
            })
            .forEach(function(subAction) {
          toReturn += '<p>'+subAction.description+'</p>';
        });
        
        toReturn += '<p>String to send: " '+action.string+' "</p>';
        toReturn += '</div></div></div>';
        html += toReturn;
    });

    return(html);
}

function generateObservationsHtml(step, observationsArray) {

  var html = '';

    observationsArray
        .forEach(function(observation) {
        html += '<div class="col-md-4">' +
          '<div class="card ob-area" data-observationId="'+observation.id+'">' +
          '<div class="card-body">';
          observation.subObservations
              .filter(function(subObservation) {
                return subObservation.name !== "";
              })
              .forEach(function(subObservation) {
              html += '<div>'+subObservation.description+'</div>';
          });
        html += '</div>' +
          '</div>' +
          '</div>';

    });

    /*html += '<div class="col-md-4">' +
      '<div class="card ob-area" data-observationId="otherObs">' +
      '<div class="card-body">'+
      '<div>Observation not present </div>';
    html += '</div>' +
      '</div>' +
      '</div>';*/

    return html;

}
/************ STEPS GENERATION ***************/

function normalizeActions(actionsArray) {
actArray = actionsArray.map(function(action) {
        var id = Object.keys(action)[0];
        return {
            id: id,
            subActions: action[id]["subActions"],
            reward: action[id]["reward"],
            string: action[id]["string"]

        };
    });

  rewardSum = 0;
  _.each(actArray, function(a) {
    rewardSum += parseFloat(a.reward);
  });
  _.each(actArray, function(a) {
    a.reward = parseFloat(a.reward) / rewardSum
  });

  return actArray
}

function normalizeObservations(observationsArray) {
    return observationsArray.map(function(observation) {
        var id = Object.keys(observation)[0];
        return {
            id: id,
            subObservations: observation[id]
        };
    });
}





function UI_init(data) {

  try {
    acjs = $('#accordion').accordionjs();
  }
  catch(error) {
    console.log("Error:" + error);
    alert("Error: "+ error);
  }

  $('#category-select').on('click', UI_categoryClicked);


  $('#subcategory-select').on('click', UI_hackingGoalClicked);

  $('#report-btn').on('click', function(event){
    $('#report-area').show();
  })

  /*$('html, body').animate({
    scrollTop: $("#bottom").offset().top
  }, 500);*/
  var obj = JSON.parse(data)
  var categories = obj.categories;
  UI_buildCategoryPanel("#categorylist_body", categories, UI_NAMECATEGORY);



    $(".accordionjs-content").on('click', '.submit-step-btn', function() {
        var $card = $(this).closest(".container-fluid");
        console.log($(this).closest(".container-fluid"));
        var observationId = $(this).closest(".container-fluid").find(".ob-area.active").data("observationid");
       if (observationId == "otherObs") {
         alert("Observation not present ... train more ;) ");
       }
        waptSendObservation(observationId)
            .then(function() {
                waptAsk(HackingGoal.cat, HackingGoal.hg, function(ret) {

                    if (ret.isFinalState == false) {
                        initStep(normalizeActions(ret.actions.actions), normalizeObservations(ret.observations.observations));
                        $("#accordionjs-page-1").animate({ scrollTop: $("#bottom").offset().top - $card.offset().top + $("#accordionjs-page-1").scrollTop()}, 500);                       
                    }
                    else if (ret.isFinalState == true) {
                        $("#finalModal").modal('show');
                    }
                });
            });
    })

}

function UI_warnUser(message) {
  $("#user_warning").removeClass("display-off")
  $($("#user_warning").find('div')[0]).text(message)
}
// function UI_reset
