# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SensorNearData/Brake.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


#import header_pb2 as header__pb2

import PB.header_pb2 as header__pb2
import PB.SensorNearData.SensorStates_pb2 as SensorNearData_dot_SensorStates__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aSensorNearData/Brake.proto\x12\x11pb.SensorNearData\x1a\x0cheader.proto\x1a!SensorNearData/SensorStates.proto\"\xcf\x02\n\x05\x42rake\x12\x1a\n\x06header\x18\x01 \x01(\x0b\x32\n.pb.Header\x12+\n\x04\x65rrs\x18\x03 \x01(\x0b\x32\x1d.pb.SensorNearData.Brake.Errs\x12\x31\n\x07signals\x18\x04 \x01(\x0b\x32 .pb.SensorNearData.Brake.Signals\x12\x36\n\ntimestamps\x18\x06 \x01(\x0b\x32\".pb.SensorNearData.Brake.Timestamp\x1a?\n\x04\x45rrs\x12\x37\n\x10is_brake_applied\x18\x02 \x01(\x0e\x32\x10.pb.SensorStates:\x0bSTATE_FAULT\x1a*\n\x07Signals\x12\x1f\n\x10is_brake_applied\x18\x03 \x01(\x08:\x05\x66\x61lse\x1a%\n\tTimestamp\x12\x18\n\x10is_brake_applied\x18\x02 \x01(\x12')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'SensorNearData.Brake_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BRAKE._serialized_start=99
  _BRAKE._serialized_end=434
  _BRAKE_ERRS._serialized_start=288
  _BRAKE_ERRS._serialized_end=351
  _BRAKE_SIGNALS._serialized_start=353
  _BRAKE_SIGNALS._serialized_end=395
  _BRAKE_TIMESTAMP._serialized_start=397
  _BRAKE_TIMESTAMP._serialized_end=434
# @@protoc_insertion_point(module_scope)