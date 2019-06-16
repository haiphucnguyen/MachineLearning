import {Component, OnInit} from '@angular/core';
import {WebcamImage} from "ngx-webcam";
import {FormBuilder, FormControl, FormGroup, Validators} from "@angular/forms";
import {HttpClient, HttpEventType, HttpHeaders} from "@angular/common/http";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit{
  title = 'frontend';
  public webcamImages: WebcamImage[] = [];
  formGroup: FormGroup;
  progress = 0;

  constructor(private httpClient: HttpClient) {

  }

  ngOnInit(): void {
    this.formGroup = new FormGroup({
    image: new FormControl(null, [Validators.required, this.requiredFileType(['png', 'jpg', 'jpeg'])])
  });
  }

  requiredFileType(types: string[] ) {
    return function (control: FormControl) {
      const file = control.value;
      if (file) {
        for (let i = 0; i < file.length; i++) {
          const extension = file.item(i).name.split('.')[1].toLowerCase();
          types.forEach(type => {
            if (type.toLowerCase() !== extension.toLowerCase() ) {
              return {
                requiredFileType: true
              };
            }
          });
        }
        return null;
      }

      return null;
    };
  }

  submit() {
    this.httpClient.post('upload', this.toFormData(this.formGroup.get('image').value), {
      reportProgress: true,
      observe: 'events'
    }).subscribe(event => {

      if ( event.type === HttpEventType.UploadProgress) {
        this.progress = Math.round((100 * event.loaded) / event.total);
      }

      if ( event.type === HttpEventType.Response ) {
        console.log(event.body);
        this.formGroup.reset();
      }

    });
  }

  toFormData<T>(formValue: T) {
    const formData = new FormData();

    for ( const key of Object.keys(formValue) ) {
      const value = formValue[key];
      console.log(key, value);
      formData.append(key, value);
    }

    return formData;
  }

  takePicture($event) {
    this.webcamImages.push($event);
  }

}
