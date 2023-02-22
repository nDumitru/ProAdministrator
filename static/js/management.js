$(document).ready(function(){
  // add new tenant button functionality
  $("#add-tenant-btn").click(function(){
    $("#add-tenant-modal").modal('show');
  });

  // add new tenant form submission
  $("#add-tenant-form").submit(function(event){
    event.preventDefault();
    $.ajax({
      type: 'POST',
      url: '/management/add-tenant/',
      data: $(this).serialize(),
      success: function(response){
        $("#add-tenant-modal").modal('hide');
        $("#add-tenant-form").trigger('reset');
        $("#tenant-table-body").prepend(response);
      },
      error: function(response){
        alert(response.responseText);
      }
    });
  });

  // edit tenant button functionality
  $(".edit-tenant-btn").click(function(){
    var tenant_id = $(this).attr('data-id');
    $.ajax({
      type: 'GET',
      url: '/management/edit-tenant/' + tenant_id,
      success: function(response){
        $("#edit-tenant-modal").modal('show');
        $("#edit-tenant-modal .modal-content").html(response);
      },
      error: function(response){
        alert(response.responseText);
      }
    });
  });

  // edit tenant form submission
  $(document).on("submit", "#edit-tenant-form", function(event){
    event.preventDefault();
    var tenant_id = $(this).attr('data-id');
    $.ajax({
      type: 'POST',
      url: '/management/edit-tenant/' + tenant_id,
      data: $(this).serialize(),
      success: function(response){
        $("#edit-tenant-modal").modal('hide');
        $("#tenant-" + tenant_id).replaceWith(response);
      },
      error: function(response){
        alert(response.responseText);
      }
    });
  });

  // delete tenant button functionality
  $(".delete-tenant-btn").click(function(){
    var tenant_id = $(this).attr('data-id');
    if(confirm("Are you sure you want to delete this tenant?")){
      $.ajax({
        type: 'POST',
        url: '/management/delete-tenant/' + tenant_id,
        success: function(response){
          $("#tenant-" + tenant_id).remove();
        },
        error: function(response){
          alert(response.responseText);
        }
      });
    }
  });
});
