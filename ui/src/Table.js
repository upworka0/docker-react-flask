import React from 'react'
import IconButton from "@material-ui/core/IconButton";
import { ReactMUIDatatable } from "react-material-ui-datatable";
import SwapHorizIcon from "@material-ui/icons/SwapHoriz";
import DeleteIcon from "@material-ui/icons/Delete";

const columns = [
  {
    name: "campaign_id",
    label: "Campaign ID"
  },
  {
    name: "created_at",
    label: "Created At"
  },
  {
    name: "current_status",
    label: "Current Status"
  },
  {
    name: "name",
    label: "Name"
  },
  {
    name: "type",
    label: "Type"
  },
  {
    name: "updated_at",
    label: "Last Updated"
  }
];

const data = [
  {"campaign_id": "9bfb9761-66f5-4946-b3d8-838b07cf7c05", "created_at": "2019-10-18T20:56:56.000Z", "current_status": "Done", "name": "Downtown - Communications - RT1", "type": "NEWSLETTER", "updated_at": "2019-10-18T22:59:54.000Z"}, {"campaign_id": "28c75c99-d2c3-420b-9cf1-b64fb0cc0f7b", "created_at": "2019-09-12T00:33:32.000Z", "current_status": "Done", "name": "Downtown - Communications", "type": "NEWSLETTER", "updated_at": "2019-10-02T00:50:19.000Z"}, {"campaign_id": "24dcac00-3f6c-4229-ae3a-cb7da46d0ad1", "created_at": "2019-08-22T16:46:54.000Z", "current_status": "Done", "name": "MONROVIA- SGV CSULA PM-Retarget", "type": "NEWSLETTER", "updated_at": "2019-08-22T19:05:11.000Z"}, {"campaign_id": "59c1e43a-3672-4371-ac02-81e946d529d1", "created_at": "2019-08-06T21:10:09.000Z", "current_status": "Done", "name": "MONROVIA- SGV CSULA PM", "type": "NEWSLETTER", "updated_at": "2019-08-07T01:05:15.000Z"}, {"campaign_id": "a17c4639-f691-4c4f-b301-ecb6c1fbc7f6", "created_at": "2019-07-11T18:18:44.000Z", "current_status": "Draft", "name": "DOWNTOWN- SGV CSULA PM Created 2019/07/08, 4:02:23 PM", "type": "NEWSLETTER", "updated_at": "2019-07-11T18:18:44.000Z"}, {"campaign_id": "c91cd83a-e09f-4205-a760-a741ba684b23", "created_at": "2019-07-08T21:02:23.000Z", "current_status": "Draft", "name": "MONROVIA- SGV CSULA PM Created 2019/07/08, 4:02:23 PM", "type": "NEWSLETTER", "updated_at": "2019-07-09T20:38:39.000Z"}
];

const customToolbarSelectActions = ({
  data,
  selectedData,
  updateSelectedData,
  handleDelete
}) => (
  <React.Fragment>
    <IconButton
      onClick={() => {
        const nextSelectedData = data.reduce((nextSelectedData, row) => {
          if (!selectedData.includes(row)) {
            nextSelectedData.push(row);
          }

          return nextSelectedData;
        }, []);

        updateSelectedData(nextSelectedData);
      }}
    >
      <SwapHorizIcon />
    </IconButton>
    <IconButton
      onClick={() => {
        handleDelete(selectedData);
      }}
    >
      <DeleteIcon />
    </IconButton>
  </React.Fragment>
);

const Demo = () => (
  <div className={"App"}>
    <ReactMUIDatatable
      title={"Campaigns"}
      data={data}
      columns={columns}
      toolbarSelectActions={customToolbarSelectActions}
    />
  </div>
);

export default Demo;


