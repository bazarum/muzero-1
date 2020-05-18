# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/replay_buffer.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tensorflow.core.framework import tensor_pb2 as tensorflow_dot_core_dot_framework_dot_tensor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/replay_buffer.proto',
  package='tensorflow',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1aprotos/replay_buffer.proto\x12\ntensorflow\x1a&tensorflow/core/framework/tensor.proto\"\x07\n\x05\x45mpty\"x\n\rStatsResponse\x12\x37\n\x07metrics\x18\x01 \x03(\x0b\x32&.tensorflow.StatsResponse.MetricsEntry\x1a.\n\x0cMetricsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\"\x1f\n\x06Policy\x12\x15\n\rprobabilities\x18\x01 \x03(\x02\"\xab\x01\n\x0bGameHistory\x12-\n\x0cobservations\x18\x01 \x03(\x0b\x32\x17.tensorflow.TensorProto\x12\x0f\n\x07\x61\x63tions\x18\x02 \x03(\x05\x12\x0f\n\x07rewards\x18\x03 \x03(\x02\x12\x10\n\x08to_plays\x18\x04 \x03(\x05\x12\x13\n\x0broot_values\x18\x05 \x03(\x02\x12$\n\x08policies\x18\x06 \x03(\x0b\x32\x12.tensorflow.Policy\"#\n\x10SaveGameResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"d\n\x10MiniBatchRequest\x12\x12\n\nbatch_size\x18\x01 \x01(\x05\x12\x18\n\x10num_unroll_steps\x18\x02 \x01(\x05\x12\x10\n\x08td_steps\x18\x03 \x01(\x05\x12\x10\n\x08\x64iscount\x18\x04 \x01(\x02\"\xbd\x02\n\x11MiniBatchResponse\x12;\n\ndatapoints\x18\x01 \x03(\x0b\x32\'.tensorflow.MiniBatchResponse.DataPoint\x1a\xea\x01\n\tDataPoint\x12,\n\x0bobservation\x18\x01 \x01(\x0b\x32\x17.tensorflow.TensorProto\x12\x0f\n\x07\x61\x63tions\x18\x02 \x03(\x05\x12H\n\x07targets\x18\x03 \x03(\x0b\x32\x37.tensorflow.MiniBatchResponse.DataPoint.DataPointTarget\x1aT\n\x0f\x44\x61taPointTarget\x12\r\n\x05value\x18\x01 \x01(\x02\x12\x0e\n\x06reward\x18\x02 \x01(\x02\x12\"\n\x06policy\x18\x03 \x01(\x0b\x32\x12.tensorflow.Policy2\xda\x01\n\x0cReplayBuffer\x12\x37\n\x05Stats\x12\x11.tensorflow.Empty\x1a\x19.tensorflow.StatsResponse\"\x00\x12\x43\n\x08SaveGame\x12\x17.tensorflow.GameHistory\x1a\x1c.tensorflow.SaveGameResponse\"\x00\x12L\n\x0bSampleBatch\x12\x1c.tensorflow.MiniBatchRequest\x1a\x1d.tensorflow.MiniBatchResponse\"\x00\x62\x06proto3')
  ,
  dependencies=[tensorflow_dot_core_dot_framework_dot_tensor__pb2.DESCRIPTOR,])




_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='tensorflow.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=82,
  serialized_end=89,
)


_STATSRESPONSE_METRICSENTRY = _descriptor.Descriptor(
  name='MetricsEntry',
  full_name='tensorflow.StatsResponse.MetricsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorflow.StatsResponse.MetricsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorflow.StatsResponse.MetricsEntry.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=165,
  serialized_end=211,
)

_STATSRESPONSE = _descriptor.Descriptor(
  name='StatsResponse',
  full_name='tensorflow.StatsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metrics', full_name='tensorflow.StatsResponse.metrics', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_STATSRESPONSE_METRICSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=91,
  serialized_end=211,
)


_POLICY = _descriptor.Descriptor(
  name='Policy',
  full_name='tensorflow.Policy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='probabilities', full_name='tensorflow.Policy.probabilities', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=213,
  serialized_end=244,
)


_GAMEHISTORY = _descriptor.Descriptor(
  name='GameHistory',
  full_name='tensorflow.GameHistory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='observations', full_name='tensorflow.GameHistory.observations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='actions', full_name='tensorflow.GameHistory.actions', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rewards', full_name='tensorflow.GameHistory.rewards', index=2,
      number=3, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='to_plays', full_name='tensorflow.GameHistory.to_plays', index=3,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='root_values', full_name='tensorflow.GameHistory.root_values', index=4,
      number=5, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='policies', full_name='tensorflow.GameHistory.policies', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=247,
  serialized_end=418,
)


_SAVEGAMERESPONSE = _descriptor.Descriptor(
  name='SaveGameResponse',
  full_name='tensorflow.SaveGameResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='tensorflow.SaveGameResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=420,
  serialized_end=455,
)


_MINIBATCHREQUEST = _descriptor.Descriptor(
  name='MiniBatchRequest',
  full_name='tensorflow.MiniBatchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='batch_size', full_name='tensorflow.MiniBatchRequest.batch_size', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_unroll_steps', full_name='tensorflow.MiniBatchRequest.num_unroll_steps', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='td_steps', full_name='tensorflow.MiniBatchRequest.td_steps', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='discount', full_name='tensorflow.MiniBatchRequest.discount', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=457,
  serialized_end=557,
)


_MINIBATCHRESPONSE_DATAPOINT_DATAPOINTTARGET = _descriptor.Descriptor(
  name='DataPointTarget',
  full_name='tensorflow.MiniBatchResponse.DataPoint.DataPointTarget',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorflow.MiniBatchResponse.DataPoint.DataPointTarget.value', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reward', full_name='tensorflow.MiniBatchResponse.DataPoint.DataPointTarget.reward', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='policy', full_name='tensorflow.MiniBatchResponse.DataPoint.DataPointTarget.policy', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=793,
  serialized_end=877,
)

_MINIBATCHRESPONSE_DATAPOINT = _descriptor.Descriptor(
  name='DataPoint',
  full_name='tensorflow.MiniBatchResponse.DataPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='observation', full_name='tensorflow.MiniBatchResponse.DataPoint.observation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='actions', full_name='tensorflow.MiniBatchResponse.DataPoint.actions', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targets', full_name='tensorflow.MiniBatchResponse.DataPoint.targets', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_MINIBATCHRESPONSE_DATAPOINT_DATAPOINTTARGET, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=643,
  serialized_end=877,
)

_MINIBATCHRESPONSE = _descriptor.Descriptor(
  name='MiniBatchResponse',
  full_name='tensorflow.MiniBatchResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='datapoints', full_name='tensorflow.MiniBatchResponse.datapoints', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_MINIBATCHRESPONSE_DATAPOINT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=560,
  serialized_end=877,
)

_STATSRESPONSE_METRICSENTRY.containing_type = _STATSRESPONSE
_STATSRESPONSE.fields_by_name['metrics'].message_type = _STATSRESPONSE_METRICSENTRY
_GAMEHISTORY.fields_by_name['observations'].message_type = tensorflow_dot_core_dot_framework_dot_tensor__pb2._TENSORPROTO
_GAMEHISTORY.fields_by_name['policies'].message_type = _POLICY
_MINIBATCHRESPONSE_DATAPOINT_DATAPOINTTARGET.fields_by_name['policy'].message_type = _POLICY
_MINIBATCHRESPONSE_DATAPOINT_DATAPOINTTARGET.containing_type = _MINIBATCHRESPONSE_DATAPOINT
_MINIBATCHRESPONSE_DATAPOINT.fields_by_name['observation'].message_type = tensorflow_dot_core_dot_framework_dot_tensor__pb2._TENSORPROTO
_MINIBATCHRESPONSE_DATAPOINT.fields_by_name['targets'].message_type = _MINIBATCHRESPONSE_DATAPOINT_DATAPOINTTARGET
_MINIBATCHRESPONSE_DATAPOINT.containing_type = _MINIBATCHRESPONSE
_MINIBATCHRESPONSE.fields_by_name['datapoints'].message_type = _MINIBATCHRESPONSE_DATAPOINT
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['StatsResponse'] = _STATSRESPONSE
DESCRIPTOR.message_types_by_name['Policy'] = _POLICY
DESCRIPTOR.message_types_by_name['GameHistory'] = _GAMEHISTORY
DESCRIPTOR.message_types_by_name['SaveGameResponse'] = _SAVEGAMERESPONSE
DESCRIPTOR.message_types_by_name['MiniBatchRequest'] = _MINIBATCHREQUEST
DESCRIPTOR.message_types_by_name['MiniBatchResponse'] = _MINIBATCHRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), dict(
  DESCRIPTOR = _EMPTY,
  __module__ = 'protos.replay_buffer_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.Empty)
  ))
_sym_db.RegisterMessage(Empty)

StatsResponse = _reflection.GeneratedProtocolMessageType('StatsResponse', (_message.Message,), dict(

  MetricsEntry = _reflection.GeneratedProtocolMessageType('MetricsEntry', (_message.Message,), dict(
    DESCRIPTOR = _STATSRESPONSE_METRICSENTRY,
    __module__ = 'protos.replay_buffer_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.StatsResponse.MetricsEntry)
    ))
  ,
  DESCRIPTOR = _STATSRESPONSE,
  __module__ = 'protos.replay_buffer_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.StatsResponse)
  ))
_sym_db.RegisterMessage(StatsResponse)
_sym_db.RegisterMessage(StatsResponse.MetricsEntry)

Policy = _reflection.GeneratedProtocolMessageType('Policy', (_message.Message,), dict(
  DESCRIPTOR = _POLICY,
  __module__ = 'protos.replay_buffer_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.Policy)
  ))
_sym_db.RegisterMessage(Policy)

GameHistory = _reflection.GeneratedProtocolMessageType('GameHistory', (_message.Message,), dict(
  DESCRIPTOR = _GAMEHISTORY,
  __module__ = 'protos.replay_buffer_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.GameHistory)
  ))
_sym_db.RegisterMessage(GameHistory)

SaveGameResponse = _reflection.GeneratedProtocolMessageType('SaveGameResponse', (_message.Message,), dict(
  DESCRIPTOR = _SAVEGAMERESPONSE,
  __module__ = 'protos.replay_buffer_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.SaveGameResponse)
  ))
_sym_db.RegisterMessage(SaveGameResponse)

MiniBatchRequest = _reflection.GeneratedProtocolMessageType('MiniBatchRequest', (_message.Message,), dict(
  DESCRIPTOR = _MINIBATCHREQUEST,
  __module__ = 'protos.replay_buffer_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.MiniBatchRequest)
  ))
_sym_db.RegisterMessage(MiniBatchRequest)

MiniBatchResponse = _reflection.GeneratedProtocolMessageType('MiniBatchResponse', (_message.Message,), dict(

  DataPoint = _reflection.GeneratedProtocolMessageType('DataPoint', (_message.Message,), dict(

    DataPointTarget = _reflection.GeneratedProtocolMessageType('DataPointTarget', (_message.Message,), dict(
      DESCRIPTOR = _MINIBATCHRESPONSE_DATAPOINT_DATAPOINTTARGET,
      __module__ = 'protos.replay_buffer_pb2'
      # @@protoc_insertion_point(class_scope:tensorflow.MiniBatchResponse.DataPoint.DataPointTarget)
      ))
    ,
    DESCRIPTOR = _MINIBATCHRESPONSE_DATAPOINT,
    __module__ = 'protos.replay_buffer_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.MiniBatchResponse.DataPoint)
    ))
  ,
  DESCRIPTOR = _MINIBATCHRESPONSE,
  __module__ = 'protos.replay_buffer_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.MiniBatchResponse)
  ))
_sym_db.RegisterMessage(MiniBatchResponse)
_sym_db.RegisterMessage(MiniBatchResponse.DataPoint)
_sym_db.RegisterMessage(MiniBatchResponse.DataPoint.DataPointTarget)


_STATSRESPONSE_METRICSENTRY._options = None

_REPLAYBUFFER = _descriptor.ServiceDescriptor(
  name='ReplayBuffer',
  full_name='tensorflow.ReplayBuffer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=880,
  serialized_end=1098,
  methods=[
  _descriptor.MethodDescriptor(
    name='Stats',
    full_name='tensorflow.ReplayBuffer.Stats',
    index=0,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_STATSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SaveGame',
    full_name='tensorflow.ReplayBuffer.SaveGame',
    index=1,
    containing_service=None,
    input_type=_GAMEHISTORY,
    output_type=_SAVEGAMERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SampleBatch',
    full_name='tensorflow.ReplayBuffer.SampleBatch',
    index=2,
    containing_service=None,
    input_type=_MINIBATCHREQUEST,
    output_type=_MINIBATCHRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_REPLAYBUFFER)

DESCRIPTOR.services_by_name['ReplayBuffer'] = _REPLAYBUFFER

# @@protoc_insertion_point(module_scope)
