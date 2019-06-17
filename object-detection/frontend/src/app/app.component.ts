import {Component, OnInit} from '@angular/core';
import {WebcamImage} from "ngx-webcam";
import {FormBuilder, FormControl, FormGroup, Validators} from "@angular/forms";
import {HttpClient, HttpEventType, HttpHeaders, HttpResponse} from "@angular/common/http";
import {DomSanitizer} from "@angular/platform-browser";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  title = 'frontend';
  public webcamImages: WebcamImage[] = [];
  formGroup: FormGroup;
  progress = 0;
  plotSrc;
  originalImg;

  constructor(private httpClient: HttpClient) {

  }

  ngOnInit(): void {
    this.formGroup = new FormGroup({
      image: new FormControl(null, [Validators.required, this.requiredFileType(['png', 'jpg', 'jpeg'])])
    });
  }

  requiredFileType(types: string[]) {
    return function (control: FormControl) {
      const file = control.value;
      console.log(file);
      if (file) {
        for (let i = 0; i < file.length; i++) {
          const extension = file.item(i).name.split('.')[1].toLowerCase();
          types.forEach(type => {
            if (type.toLowerCase() !== extension.toLowerCase()) {
              return {
                requiredFileType: true
              };
            }
          });
        }
        return null;
      }
      return {
        requiredFileType: true
      };
    };
  }

  submit() {
    let formValue = this.formGroup.get('image').value;
    if (!formValue) {
      return;
    }
    this.uploadAndDetectObject(formValue);
  }

  private uploadAndDetectObject(formValue) {
    this.httpClient.post('upload', this.toFormData(formValue), {
      reportProgress: true,
      observe: 'events',
      responseType: 'blob' as 'json'
    }).subscribe(event => {

      if (event.type === HttpEventType.UploadProgress) {
        this.progress = Math.round((100 * event.loaded) / event.total);
      }

      if (event.type === HttpEventType.Response) {
        console.log(event.body);
        this.formGroup.reset();
        this.formGroup.controls['image'].setValue(null);
        this.createImageFromBlob(<Blob>event.body);

      }

    });
  }

  uploadFromWebcam() {
    let files: File[] = [];
    this.webcamImages.forEach(wcImg => {
      this.originalImg = wcImg.imageAsDataUrl;
      let blob = this.dataURItoBlob(wcImg.imageAsDataUrl);
      let date = new Date();
      let timestamp = date.getTime();
      files.push(new File([blob], timestamp + '.png', {type: 'image/png'}));
    });
    this.uploadAndDetectObject(files);
  }

  dataURItoBlob(dataURI) {
    // convert base64/URLEncoded data component to raw binary data held in a string
    var byteString;
    if (dataURI.split(',')[0].indexOf('base64') >= 0)
      byteString = atob(dataURI.split(',')[1]);
    else
      byteString = unescape(dataURI.split(',')[1]);

    // separate out the mime component
    var mimeString = dataURI.split(',')[0].split(':')[1].split(';')[0];

    // write the bytes of the string to a typed array
    var ia = new Uint8Array(byteString.length);
    for (var i = 0; i < byteString.length; i++) {
      ia[i] = byteString.charCodeAt(i);
    }

    return new Blob([ia], {type: mimeString});
  }


  toFormData<T>(formValue: T) {
    const formData = new FormData();
    for (const key of Object.keys(formValue)) {
      const value = formValue[key];
      console.log((<ImageData>value));
      this.originalImg = (<HTMLImageElement>value).src;
      formData.append(key, value);
    }

    return formData;
  }

  takePicture($event) {
    this.webcamImages.push($event);
  }

  createImageFromBlob(image: Blob) {
    let reader = new FileReader();
    reader.addEventListener("load", () => {
      this.plotSrc = reader.result;
    }, false);
    if (image) {
      reader.readAsDataURL(image);
    }
  }

}
