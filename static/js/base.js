$(document).ready(function () {
  // Toggle sidebar
  $("#sidebar-toggle-btn").click(function () {
    $("#sidebar-wrapper").toggleClass("hide-sidebar");
    $("#content-wrapper").toggleClass("full-width");
    $(this).toggleClass("active");
  });

  // Datatables initialization
  $(".data-table").DataTable({
    responsive: true,
    paging: false,
    searching: false,
    info: false,
    columnDefs: [
      {
        targets: "no-sort",
        orderable: false,
      },
    ],
    language: {
      emptyTable: "No data available in table",
      zeroRecords: "No matching records found",
      info: "Showing _START_ to _END_ of _TOTAL_ entries",
      infoEmpty: "Showing 0 to 0 of 0 entries",
      lengthMenu: "Show _MENU_ entries",
      search: "Search:",
      infoFiltered: "(filtered from _MAX_ total records)",
      paginate: {
        first: "First",
        last: "Last",
        next: "Next",
        previous: "Previous",
      },
    },
  });

  // Confirmation dialogs for delete buttons
  $(".delete-btn").click(function () {
    var deleteUrl = $(this).data("url");
    var deleteText = $(this).data("text");
    bootbox.confirm({
      title: "Delete",
      message: "Are you sure you want to delete " + deleteText + "?",
      buttons: {
        cancel: {
          label: '<i class="fa fa-times"></i> Cancel',
          className: "btn-default",
        },
        confirm: {
          label: '<i class="fa fa-check"></i> Confirm',
          className: "btn-danger",
        },
      },
      callback: function (result) {
        if (result) {
          window.location.href = deleteUrl;
        }
      },
    });
  });

  // Input mask for phone number
  $("#phone-number-input").inputmask("(999) 999-9999");
});
