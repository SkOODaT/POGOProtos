# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/confirm_trading_message.proto

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
  name='pogoprotos/networking/requests/messages/confirm_trading_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_pb=_b('\nEpogoprotos/networking/requests/messages/confirm_trading_message.proto\x12\'pogoprotos.networking.requests.messages\"C\n\x15\x43onfirmTradingMessage\x12\x11\n\tplayer_id\x18\x01 \x01(\t\x12\x17\n\x0ftransaction_log\x18\x02 \x01(\tb\x06proto3')
)




_CONFIRMTRADINGMESSAGE = _descriptor.Descriptor(
  name='ConfirmTradingMessage',
  full_name='pogoprotos.networking.requests.messages.ConfirmTradingMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_id', full_name='pogoprotos.networking.requests.messages.ConfirmTradingMessage.player_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transaction_log', full_name='pogoprotos.networking.requests.messages.ConfirmTradingMessage.transaction_log', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=114,
  serialized_end=181,
)

DESCRIPTOR.message_types_by_name['ConfirmTradingMessage'] = _CONFIRMTRADINGMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConfirmTradingMessage = _reflection.GeneratedProtocolMessageType('ConfirmTradingMessage', (_message.Message,), dict(
  DESCRIPTOR = _CONFIRMTRADINGMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.confirm_trading_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.ConfirmTradingMessage)
  ))
_sym_db.RegisterMessage(ConfirmTradingMessage)


# @@protoc_insertion_point(module_scope)
