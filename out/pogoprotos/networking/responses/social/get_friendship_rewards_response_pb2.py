# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/social/get_friendship_rewards_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/social/get_friendship_rewards_response.proto',
  package='pogoprotos.networking.responses.social',
  syntax='proto3',
  serialized_pb=_b('\nLpogoprotos/networking/responses/social/get_friendship_rewards_response.proto\x12&pogoprotos.networking.responses.social\"\xaf\x02\n\x1cGetFriendshipRewardsResponse\x12[\n\x06result\x18\x01 \x01(\x0e\x32K.pogoprotos.networking.responses.social.GetFriendshipRewardsResponse.Result\x12\x11\n\txp_reward\x18\x02 \x01(\x03\x12\x11\n\tfriend_id\x18\x03 \x01(\t\"\x8b\x01\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x11\n\rERROR_UNKNOWN\x10\x02\x12\x15\n\x11\x45RROR_NOT_FRIENDS\x10\x03\x12#\n\x1f\x45RROR_MILESTONE_ALREADY_AWARDED\x10\x04\x12\x1a\n\x16\x45RROR_FAILED_TO_UPDATE\x10\x05\x62\x06proto3')
)



_GETFRIENDSHIPREWARDSRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.social.GetFriendshipRewardsResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_UNKNOWN', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_NOT_FRIENDS', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_MILESTONE_ALREADY_AWARDED', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_FAILED_TO_UPDATE', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=285,
  serialized_end=424,
)
_sym_db.RegisterEnumDescriptor(_GETFRIENDSHIPREWARDSRESPONSE_RESULT)


_GETFRIENDSHIPREWARDSRESPONSE = _descriptor.Descriptor(
  name='GetFriendshipRewardsResponse',
  full_name='pogoprotos.networking.responses.social.GetFriendshipRewardsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.social.GetFriendshipRewardsResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='xp_reward', full_name='pogoprotos.networking.responses.social.GetFriendshipRewardsResponse.xp_reward', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='friend_id', full_name='pogoprotos.networking.responses.social.GetFriendshipRewardsResponse.friend_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GETFRIENDSHIPREWARDSRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=424,
)

_GETFRIENDSHIPREWARDSRESPONSE.fields_by_name['result'].enum_type = _GETFRIENDSHIPREWARDSRESPONSE_RESULT
_GETFRIENDSHIPREWARDSRESPONSE_RESULT.containing_type = _GETFRIENDSHIPREWARDSRESPONSE
DESCRIPTOR.message_types_by_name['GetFriendshipRewardsResponse'] = _GETFRIENDSHIPREWARDSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetFriendshipRewardsResponse = _reflection.GeneratedProtocolMessageType('GetFriendshipRewardsResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETFRIENDSHIPREWARDSRESPONSE,
  __module__ = 'pogoprotos.networking.responses.social.get_friendship_rewards_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.social.GetFriendshipRewardsResponse)
  ))
_sym_db.RegisterMessage(GetFriendshipRewardsResponse)


# @@protoc_insertion_point(module_scope)
