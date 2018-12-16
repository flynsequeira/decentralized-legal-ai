import { Component, OnInit } from '@angular/core';
import { RestService } from '../../shared/services/rest.service';

@Component({
    selector: 'app-dashboard',
    templateUrl: './dashboard.component.html',
    styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {
    userQuery: String;
    demoDataset = {
        "sentiment": {
            "document": {
             "score": -0.479108,
             "label": "negative"
            }
        },
        "emotion": {
            "document": {
                "emotion": {
                    "sadness": 0.494381,
                    "joy": 0.475491,
                    "fear": 0.088296,
                    "disgust": 0.127116,
                    "anger": 0.133539
                }
            }
        }
    };
    constructor(private _rest: RestService) {
    }

    ngOnInit() {}

    submitForm() {
        console.log(this.userQuery);

        this._rest.sendLegalData(this.userQuery).subscribe( resp => {
            console.log(resp);
        },
        err => {
            console.log(err);
        });

    }

}
