let mycss = document.createElement("link");
mycss.rel = "stylesheet";
mycss.type = "text/css";
mycss.href = "/static/assets/css/style.admin.css";
document.querySelector("head").appendChild(mycss);
document.addEventListener("DOMContentLoaded", (evvent) => {
    try {
        let tinymcelist = ["#id_content", "#event_form #id_description","#product_form #id_description"]
        tinymcelist.forEach((v, k, p) => {
            try {
                document.querySelector(v).classList.add("tinymce-editor");
            } catch (error) {  
            }
        })
    } catch (error) {
        console.error(error)
    }
    
  /**
   * Initiate TinyMCE Editor
   */
  var useDarkMode = window.matchMedia("(prefers-color-scheme: dark)").matches;

  tinymce.init({
    selector: "textarea.tinymce-editor",
    plugins:
      "print preview paste importcss searchreplace autolink autosave save directionality code visualblocks visualchars fullscreen image link media template codesample table charmap hr pagebreak nonbreaking anchor toc insertdatetime advlist lists wordcount imagetools textpattern noneditable help charmap quickbars emoticons",
    imagetools_cors_hosts: ["picsum.photos"],
    menubar: "file edit view insert format tools table help",
    toolbar:
      "undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft aligncenter alignright alignjustify | outdent indent |  numlist bullist | forecolor backcolor removeformat | pagebreak | charmap emoticons | fullscreen  preview save print | insertfile image media template link anchor codesample | ltr rtl",
    toolbar_sticky: true,
    autosave_ask_before_unload: true,
    autosave_interval: "30s",
    autosave_prefix: "{path}{query}-{id}-",
    autosave_restore_when_empty: false,
    autosave_retention: "2m",
    image_advtab: true,
    link_list: [
      {
        title: "My page 1",
        value: "https://www.tiny.cloud",
      },
      {
        title: "My page 2",
        value: "http://www.moxiecode.com",
      },
    ],
    image_list: [
      {
        title: "My page 1",
        value: "https://www.tiny.cloud",
      },
      {
        title: "My page 2",
        value: "http://www.moxiecode.com",
      },
    ],
    image_class_list: [
      {
        title: "None",
        value: "",
      },
      {
        title: "Some class",
        value: "article_img",
      },
    ],
    importcss_append: true,
    file_picker_callback: function (callback, value, meta) {
      /* Provide file and text for the link dialog */
      if (meta.filetype === "file") {
        callback("https://www.google.com/logos/google.jpg", {
          text: "My text",
        });
      }

      /* Provide image and alt text for the image dialog */
      if (meta.filetype === "image") {
        let img_uploader = document.createElement("input");
        img_uploader.type = "file";
        img_uploader.accept = "image/*";
        img_uploader.style.display = "none";
        img_uploader.addEventListener("change", (event) => {
          var files = event.target.files;
          if (files.length === 0) {
            console.log("No files selected");
            return;
          }
          var reader = new FileReader();
          reader.onload = function (eve) {
            callback(eve.target.result, { width: "100%", height: "auto" });
            img_uploader.remove();
          };
          reader.readAsDataURL(files[0]);
        });
        document.body.appendChild(img_uploader);
        img_uploader.click();

        //callback("https://www.google.com/logos/google.jpg", {
        //  alt: "My alt text",
        //});
      }

      /* Provide alternative source and posted for the media dialog */
      if (meta.filetype === "media") {
        callback("movie.mp4", {
          source2: "alt.ogg",
          poster: "https://www.google.com/logos/google.jpg",
        });
      }
    },
    templates: [
      {
        title: "New Table",
        description: "creates a new table",
        content:
          '<div class="mceTmpl"><table width="98%%"  border="0" cellspacing="0" cellpadding="0"><tr><th scope="col"> </th><th scope="col"> </th></tr><tr><td> </td><td> </td></tr></table></div>',
      },
      {
        title: "Starting my story",
        description: "A cure for writers block",
        content: "Once upon a time...",
      },
      {
        title: "New list with dates",
        description: "New List with dates",
        content:
          '<div class="mceTmpl"><span class="cdate">cdate</span><br /><span class="mdate">mdate</span><h2>My List</h2><ul><li></li><li></li></ul></div>',
      },
    ],
    template_cdate_format: "[Date Created (CDATE): %m/%d/%Y : %H:%M:%S]",
    template_mdate_format: "[Date Modified (MDATE): %m/%d/%Y : %H:%M:%S]",
    height: 600,
    image_caption: true,
    quickbars_selection_toolbar:
      "bold italic | quicklink h2 h3 blockquote quickimage quicktable",
    noneditable_noneditable_class: "mceNonEditable",
    toolbar_mode: "sliding",
    contextmenu: "link image imagetools table",
    skin: useDarkMode ? "oxide-dark" : "oxide",
    content_css: useDarkMode ? "dark" : "default",
    init_instance_callback: function (editor) {
      console.log(editor);
    },
    content_style:
      "body { font-family:Helvetica,Arial,sans-serif; font-size:14px }",
  });


    try {
        document.querySelectorAll(`textarea[name="image"]`).forEach((v, k, p) => {
            imageWidget(v);
        });
        imageWidget(document.querySelector("#event_form #id_front_image"))
    } catch (error) {
        
    }
    

  function imageWidget(el) {
    el.style.display = "none";
    let prnt = el.parentElement;
    let btn = document.createElement("img");
      btn.classList.add("img_widget_img");
    btn.alt = "Click here to add Image...";
    btn.src = el.value;
    btn.onclick = (event) => {
      let img_uploader = document.createElement("input");
      img_uploader.type = "file";
      img_uploader.accept = "image/*";
      img_uploader.style.display = "none";
      img_uploader.addEventListener("change", (evnt) => {
        var files = evnt.target.files;
        if (files.length === 0) {
          console.log("No files selected");
          return;
        }
        var reader = new FileReader();
        reader.onload = function (eve) {
            el.value = (eve.target.result);
            btn.src = (eve.target.result);
          img_uploader.remove();
        };
        reader.readAsDataURL(files[0]);
      });
      document.body.appendChild(img_uploader);
      img_uploader.click();
      };
      prnt.appendChild(btn);
  }
});
