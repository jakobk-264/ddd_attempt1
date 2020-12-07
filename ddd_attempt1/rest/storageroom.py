import json
from flask import Blueprint, Response

from ddd_attempt1.shared import request_object as req
from ddd_attempt1.repository import memrepo as mr
from ddd_attempt1.use_cases import storageroom_use_cases as uc
from ddd_attempt1.serializers import storageroom_serializer as ser

blueprint = Blueprint('storageroom', __name__)


@blueprint.route('/storagerooms', methods=['GET'])
def storageroom():
    request_object = req.StorageRoomListRequestObject.from_dict({})

    repo = mr.MemRepo()
    use_case = uc.StorageRoomListUseCase(repo)

    response = use_case.execute(request_object)

    return Response(
        json.dumps(response.value, cls=ser.StorageRoomEncoder),
        mimetype='application/json',
        status=200
    )
