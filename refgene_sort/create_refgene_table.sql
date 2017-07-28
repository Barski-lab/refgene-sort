DROP TABLE IF EXISTS `refGene`;
CREATE TABLE `refGene` (
      `bin` smallint(5) NOT NULL,
      `name` varchar(255) NOT NULL,
      `chrom` varchar(255) NOT NULL,
      `strand` char(1) NOT NULL,
      `txStart` int(10) NOT NULL,
      `txEnd` int(10) NOT NULL,
      `cdsStart` int(10) NOT NULL,
      `cdsEnd` int(10) NOT NULL,
      `exonCount` int(10) NOT NULL,
      `exonStarts` longblob NOT NULL,
      `exonEnds` longblob NOT NULL,
      `score` int(11) DEFAULT NULL,
      `name2` varchar(255) NOT NULL,
      `cdsStartStat` varchar(255) NOT NULL,
      `cdsEndStat` varchar(255) NOT NULL,
      `exonFrames` longblob NOT NULL
  )
