# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/player/user_issue_weather_report.proto

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
  name='pogoprotos/data/player/user_issue_weather_report.proto',
  package='pogoprotos.data.player',
  syntax='proto3',
  serialized_pb=_b('\n6pogoprotos/data/player/user_issue_weather_report.proto\x12\x16pogoprotos.data.player\"q\n\x16UserIssueWeatherReport\x12\x1a\n\x12gameplayer_weather\x18\x01 \x01(\t\x12\x14\n\x0c\x61lert_active\x18\x02 \x01(\x08\x12\x10\n\x08severity\x18\x03 \x01(\x05\x12\x13\n\x0buser_report\x18\x04 \x01(\x05\x62\x06proto3')
)




_USERISSUEWEATHERREPORT = _descriptor.Descriptor(
  name='UserIssueWeatherReport',
  full_name='pogoprotos.data.player.UserIssueWeatherReport',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gameplayer_weather', full_name='pogoprotos.data.player.UserIssueWeatherReport.gameplayer_weather', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='alert_active', full_name='pogoprotos.data.player.UserIssueWeatherReport.alert_active', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='severity', full_name='pogoprotos.data.player.UserIssueWeatherReport.severity', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_report', full_name='pogoprotos.data.player.UserIssueWeatherReport.user_report', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=82,
  serialized_end=195,
)

DESCRIPTOR.message_types_by_name['UserIssueWeatherReport'] = _USERISSUEWEATHERREPORT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserIssueWeatherReport = _reflection.GeneratedProtocolMessageType('UserIssueWeatherReport', (_message.Message,), dict(
  DESCRIPTOR = _USERISSUEWEATHERREPORT,
  __module__ = 'pogoprotos.data.player.user_issue_weather_report_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.player.UserIssueWeatherReport)
  ))
_sym_db.RegisterMessage(UserIssueWeatherReport)


# @@protoc_insertion_point(module_scope)
