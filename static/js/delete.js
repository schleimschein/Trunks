(function() {
  var deleteContainers  = document.getElementsByClassName('has-delete');

  for(var i = 0; i < deleteContainers.length; i++)
  {
      var deleteContainer = deleteContainers[i];
      var deletes = deleteContainer.getElementsByClassName('delete');

      for(var j = 0; j < deletes.length; j++)
      {
        var dlt = deletes[j];

        dlt.onclick = function()
        {
            deleteContainer.remove();
        }
      }
  }
})();